from proc_init import ProcDDEXRec
from node_proc.proc_mods.message_header import message_header_38


# Las keys del diccionario son los nombres de los nodos que se procesan y
# los valores son las funciones que procesan esos nodos KEYNAME_VERSION.

processor_methods = {
    'message_header': message_header_38,
}


# Example usage:
with ProcDDEXRec() as o:
    o.set_instance_methods(processor_methods)
    o.proc_ddex('./xml_files/ddex38.xml')

# processor_methods = {
#     "message_thread_id": message_thread_id_42,
#     "message_id": message_id_42,
#     "message_sender_id": sender_id_42,
#     "message_sender_name": sender_name_42,
#     "message_recipient_id": recipient_id_42,
#     "message_recipient_name": recipient_name_42,
#     "message_created_datetime": created_datetime_42,
#     "message_control_type": control_type_42,
# }