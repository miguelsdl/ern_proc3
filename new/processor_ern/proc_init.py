import xmltodict
import json
import re
import inspect
import types
from db.models.album import Album
from db.db.session import SessionLocal



class ProcDDEXJSON:
    def __init__(self):
        self.ddex_version = None
        self.album = Album()
        self.session = SessionLocal()

        print("Iniciando ProcDDEXJSON")

    def collect_all_values(self):
        """Devuelve un diccionario con todas las variables de instancia que terminan en '_value'."""
        return {attr: getattr(self, attr) for attr in self.__dict__ if attr.endswith('_value')}

    def save_output_json(self, archivo='output.json'):
        datos = self.collect_all_values()
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def save_input_json(self, data, archivo='input.json'):
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def set_instance_methods(self, methods):
        for method_name, method_definition in methods.items():
            # Crea un método en la instancia con el nombre del método y la función proporcionada.
            self.__setattr__(method_name, method_definition.get('func'))
            # Si el método tiene parámetros, los guarda como un atributo de la instancia.
            self.__setattr__('{}_params'.format(method_name), method_definition.get('params', {}))

    def proc_ddex(self, filename) -> bool:
        """Procesa el archivo XML recorriendo recursivamente los nodos."""
        with open(filename, 'r', encoding='utf-8') as xml_file:
            xml_content = xml_file.read()
            data = xmltodict.parse(xml_content)
            self.save_input_json(data)

            version = self.extract_ddex_ern_version(data)
            if version == '43':
                run = True
                proc_module = 'proc_mods.ddex_43'
            elif version == '383':
                run = True
                proc_module = 'proc_mods.ddex_383'
            else:
                run = False
            print(version)

            if run:
                proc_methods = self.extract_functions_from_module(__import__(proc_module, fromlist=['']))
                module = __import__(proc_module, fromlist=[''])
                processor_methods = {name: {'func': getattr(module, name), 'params': {}} for name in proc_methods}
                self.set_instance_methods(processor_methods)

            self.recurse_json(data=data)
            # self.album.save(session=self.session)
            self.album.save_all(session=self.session)
        return True

    def recurse_json(self, data, path=""):
        if isinstance(data, dict):
            for key, value in data.items():
                new_path = f"{path}.{key}" if path else key

                if key in {'MessageHeader', 'Party', 'SoundRecording', 'Release', 'DealList'}:
                    print(key)
                if key in {'TrackRelease'}:
                    print(key)

                self._case_filter(key=key, node=value, current_path=new_path)
                self.recurse_json(value, new_path)
                ''' Acá lleno la estructura generalizada'''
        elif isinstance(data, list):
            for index, item in enumerate(data):
                new_path = f"{path}[{index}]"
                self.recurse_json(item, new_path)
        # else:
        #     print(f"{path}: {data}")

    def _case_filter(self, key=None, node=None, current_path=None):

        method_name = ProcDDEXJSON.pascal_to_snake_case(key)
        if hasattr(self, method_name):
            params = getattr(self, '{}_params'.format(method_name))
            vars_values = self.collect_all_values()
            params.update(vars_values)
            value = self.__getattribute__(method_name)(self, node, **params)
            var_name = "{}_value".format(method_name)
            if isinstance(value, str) or isinstance(value, int) or isinstance(value, float):
                # Si es str, int o float, lo reemplazo.
                self.__setattr__("{}_value".format(method_name), value)
            elif isinstance(value, dict):
                # si es dict, lo actualizo.
                new_value = self.__getattribute__(var_name) if hasattr(self, var_name) else {}
                if 'add_as_instance_var' in value:
                    # Si el diccionario tiene la clave 'add_as_instance_var', lo agrego como variable de instancia,
                    # esto es para los nodos que tienen mucha información anidada.
                    for key, val in value['add_as_instance_var'].items():
                        self.__setattr__(f"{key}_value", val)
                        # print(f"{key}: {val}")
                # Actualizo el valor del lo que viene en la key result.
                new_value.update(value.get('result', {}))
                self.__setattr__("{}_value".format(method_name), new_value)
            elif isinstance(value, list):
                # Si es lista, lo extiendo.
                new_value = self.__getattribute__(var_name) if hasattr(self, var_name) else []
                new_value.extend(value)
                self.__setattr__("{}_value".format(method_name), new_value)
            else:
                # Si no es ninguno de los anteriores, lanzo un error.
                raise TypeError(
                    "{} tipo no reconocido en el else del método proc.ProcDDEXRec.case_filter()".format(value)
                )

            # print(var_name, ':', self.__getattribute__("{}_value".format(method_name)))

    @staticmethod
    def pascal_to_snake_case(s: str) -> str:
        """Pasa de CamelCase o PascalCase a snake_case."""
        return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

    def clean_values(self):
        print("atributos que terminan en _value:")
        for attr in list(self.__dict__):
            if attr.endswith('_value'):
                print(attr, ':', json.dumps(self.__getattribute__(attr)))
                # print(f"Limpiando {attr}")
                # delattr(self, attr)

    def __enter__(self):
        print("Iniciando parseo XML")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("🚪 Terminando y limpiando")
        self.save_output_json()
        self.clean_values()

    def extract_functions_from_module(self, mod):
        return [name for name, obj in inspect.getmembers(mod) if isinstance(obj, types.FunctionType)]

    def extract_ddex_ern_version(self, data):
        if not isinstance(data, dict):
            return None

        message_key = next((k for k in data if "NewReleaseMessage" in k), None)
        if not message_key:
            return None

        attrs = data.get(message_key, {})
        possible_values = list(attrs.values())

        for val in possible_values:
            if isinstance(val, str) and "ddex.net/xml/ern/" in val:
                match = re.search(r"ern/(\d+)", val)
                if match:
                    return match.group(1)

        return None

def tarea(n):
    with ProcDDEXJSON() as o:
        o.proc_ddex(filename='./xml/A10301A0000935334X.xml')
        # o.proc_ddex(filename='../xml_files/A10301A0003476861G.xml')
        # o.proc_ddex(filename='../xml_files/A10301A0000935334X.xml')
        # with open('../xml_files/A10301A0000935334X.xml', 'r', encoding='utf-8') as xml_file:
        # with open('../xml_files/A10301A0003476861G.xml', 'r', encoding='utf-8') as xml_file:
        # with open('../xml_others/ddex383_album.xml', 'r', encoding='utf-8') as xml_file:
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
def ejecutar_en_paralelo():
    resultados = []
    tareas = list(range(200))  # Por ejemplo, 10 tareas con input 0..9

    with ThreadPoolExecutor(max_workers=40) as executor:
        futuros = {executor.submit(tarea, n): n for n in tareas}

        for futuro in as_completed(futuros):
            resultado = futuro.result()
            resultados.append(resultado)

    print("🎯 Resultados:", resultados)


def medir(func, *args, **kwargs):
    import time
    import os
    import psutil

    process = psutil.Process(os.getpid())
    start_time = time.time()
    start_mem = process.memory_info().rss

    result = func(*args, **kwargs)

    end_time = time.time()
    end_mem = process.memory_info().rss

    print(f"⏱ Duración: {end_time - start_time:.20f} segundos")
    print(f"🧠 Memoria usada: {(end_mem - start_mem) / 1024 / 1024:.20f} MB")

    return result

medir(ejecutar_en_paralelo)