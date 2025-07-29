# ¡OJO!: este metodo no tiene self porque no se llama directamente en _case_filter,
# sino que se llama desde sound_recording.

def contributors(data=None, party_value=None, **kwargs):
    """Processes a list of contributors and extracts sequence number, party reference, and roles."""
    raw_contributors = data #.get("Contributor", [])
    if isinstance(raw_contributors, dict):
        raw_contributors = [raw_contributors]

    result = {}

    for contributor in raw_contributors:
        raw_roles = contributor.get("Role", [])
        if isinstance(raw_roles, dict):
            raw_roles = [raw_roles]
        elif isinstance(raw_roles, str):
            raw_roles = [raw_roles]

        roles = []
        for role in raw_roles:
            if isinstance(role, str):
                roles.append(role)
            elif isinstance(role, dict):
                if role.get("#text") == "UserDefined" and "@UserDefinedValue" in role:
                    roles.append(role["@UserDefinedValue"])
                elif role.get("#text") and role["#text"] != "UserDefined":
                    roles.append(role["#text"])
                elif "@UserDefinedValue" in role:
                    roles.append(role["@UserDefinedValue"])

        result[contributor["ContributorPartyReference"]] = {
            "sequence_number": contributor.get("@SequenceNumber"),
            "party_reference": contributor.get("ContributorPartyReference"),
            "name": party_value.get(contributor["ContributorPartyReference"], {}),
            "roles": roles
        }

    return result


'''
Prompt:

hay que modificar este metodo para que procese varios tipos de nodos que pueden venir en el json,

Cuando soloo viene un rol, en est caso no es una lista, sino un diccionario con el rol y el namespace, por ejemplo:
{
  "@SequenceNumber": "4",
  "ContributorPartyReference": "P_ARTIST_137673",
  "Role": {
    "@Namespace": "DPID:PADPIDA2007040502I",
    "@UserDefinedValue": "Guitar",
    "#text": "UserDefined"
  }
},

Cuando contributor tiene solo un elemento, por lo cual no es una lista

"Contributor":
{
  "@SequenceNumber": "1",
  "ContributorPartyReference": "P_ARTIST_2730203",
  "Role": [
    {
      "@Namespace": "DPID:PADPIDA2007040502I",
      "@UserDefinedValue": "Harmonica",
      "#text": "UserDefined"
    },
    {
      "@Namespace": "DPID:PADPIDA2007040502I",
      "@UserDefinedValue": "Keyboards",
      "#text": "UserDefined"
    },
    {
      "@Namespace": "DPID:PADPIDA2007040502I",
      "@UserDefinedValue": "Percussion",
      "#text": "UserDefined"
    },
    {
      "@Namespace": "DPID:PADPIDA2007040502I",
      "@UserDefinedValue": "Vocal",
      "#text": "UserDefined"
    },
    "Composer",
    "Lyricist"
  ]
},



Ejemplos con error

{
  "@SequenceNumber": "4",
  "ContributorPartyReference": "P_ARTIST_137673",
  "Role": {
    "@Namespace": "DPID:PADPIDA2007040502I",
    "@UserDefinedValue": "Guitar",
    "#text": "UserDefined"
  }
},

Fijate que aca no esta el rol
"P_ARTIST_137673": {
    "sequence_number": "4",
    "party_reference": "P_ARTIST_137673",
    "roles": [
        "@Namespace", 
        "@UserDefinedValue",
        "#text"
    ]
},








'''