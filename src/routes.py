import email_routes
from functools import partial
from fastapi import FastAPI, APIRouter


def initialize(app: FastAPI | APIRouter):
    print("inside init")
    
    service_value = "email-builder-service"

    base_path = "/" + service_value
    router = APIRouter(prefix=base_path)
    
    router.add_api_route(
        path="/generate",
        endpoint=partial(email_routes.generate),
        methods=["POST"],
    )
    
    app.include_router(router)
    return app





# # from mcr_py_copilot_service.src.route import copilot_routes
# import email_routes
# from functools import partial
# from fastapi import FastAPI, APIRouter
# from mcr_py_common.common_server_config.mcr_service_meta import PyMcrServiceMeta
# from mcr_py_common.common_server_config.event_bus import eventbus
# from mcr_py_common.common_server_config.mcr_common_service_list import (
#     get_mcr_service_name_by_devops_name,
#     MCR_PY_SERVICES,
# )

# def initialize(app: FastAPI | APIRouter, meta: PyMcrServiceMeta):
#     print("inside init")
#     # if meta:
#     #     eventbus.emit(
#     #         get_mcr_service_name_by_devops_name(
#     #             MCR_PY_SERVICES.MCR_PY_COPILOT_SERVICE.value
#     #         )
#     #         + "_emit",
#     #         meta,
#     #     )
#     base_path = "/email-builder-service"
#     router = APIRouter(prefix=base_path)
#     router.add_api_route(
#         path="/generate",
#         endpoint=partial(email_routes.generate),
#         methods=["POST"],
#     )

#     app.include_router(router)
#     return app