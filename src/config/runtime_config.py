# import os
# from typing import Any, Dict, List
# from dotenv import load_dotenv, find_dotenv
# from mcr_py_common.common_server_config.event_bus import eventbus
# from mcr_py_common.common_server_config.mcr_service_meta import PyMcrServiceMeta
# from mcr_py_common.common_server_config.mcr_common_service_list import (
#     get_mcr_service_name_by_devops_name,
#     MCR_PY_SERVICES,
# )
# from mcr_py_common.server_config.env_variables import config

# load_dotenv(find_dotenv(".env"))

# node_env = os.getenv("NODE_ENV", "local")
# env_specific_path = find_dotenv(f".env.{node_env}")
# if env_specific_path:
#     load_dotenv(env_specific_path, override=True)


# VAR_MAPPING: Dict[str, str] = { 
#     "crm_openai_vector_store_id" :"CRM_OPENAI_VECTOR_STORE_ID"
# }

# def get_var_by_env(env_var: str) -> List[str]:
#     return [k for k, v in VAR_MAPPING.items() if v == env_var]


# ENV_VARS = list(set(VAR_MAPPING.values()))


# default_config: Dict[str, Any] = {
#     "mongo_conn": os.getenv("CRM_MONGO_DB_CONN_STRING_TEMPLATE", "").replace(
#         "{{dbname}}", os.getenv("CRM_MONGO_DB_NAME", "")
#     ),
#     "mongo_db_name":os.getenv("CRM_MONGO_DB_NAME")
# }

# for env in ENV_VARS:
#     keys = get_var_by_env(env)
#     for k in keys:
#         default_config[k] = os.getenv(env)


# _runtime_overrides: Dict[str, Any] = {}


# class RuntimeConfig:
#     def __init__(self, base_config: Dict[str, Any]):
#         self._base_config = base_config

#     def override(self, key: str, value: Any):
#         _runtime_overrides[key] = value

#     def __getattr__(self, name: str) -> Any:
#         if name in _runtime_overrides:
#             return _runtime_overrides[name]
#         if name in self._base_config:
#             return self._base_config[name]
#         raise AttributeError(f"RuntimeConfig has no attribute '{name}'")

# merge_config = {
#     **config,   
#     **default_config       
# }

# runtime_config = RuntimeConfig(merge_config)


# @eventbus.on(
#     get_mcr_service_name_by_devops_name(MCR_PY_SERVICES.MCR_PY_COPILOT_SERVICE.value)
#     + "_emit"
# )
# def on_service_meta(meta: PyMcrServiceMeta):

#     if meta:
#         for item in meta.envs or []:
#             key = item.key
#             value = item.value
#             if item.key == "CRM_MONGO_DB_NAME":
#                 runtime_config.override("mongo_conn", os.getenv("CRM_MONGO_DB_CONN_STRING_TEMPLATE", "").replace("{{dbname}}", item.value))
#             if item.key == "CRM_OPENAI_VECTOR_STORE_ID":
#                 runtime_config.override("crm_openai_vector_store_id", item.value)

#             for config_key in get_var_by_env(key):
#                 runtime_config.override(config_key, value)
                     