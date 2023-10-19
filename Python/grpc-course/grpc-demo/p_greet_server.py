from concurrent import futures
import time

import grpc
import p_greet_pb2
import p_greet_pb2_grpc

class P_GREETERSERVICER(p_greet_pb2_grpc.P_GREETERServicer):
    def Greet(self, request, context):
        print("Request made")
        payload = {
            "message": f"{request.name} is saying {request.greeting}"
        }
        print(request)
        response = p_greet_pb2.GreetResponse(**payload)
        # response.message = f"{request.name} is saying {request.greeting}"
        return response

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    p_greet_pb2_grpc.add_P_GREETERServicer_to_server(P_GREETERSERVICER(), server)
    server.add_insecure_port("localhost:50055")
    server.start()
    server.wait_for_termination()
    
if __name__ == "__main__":
    server()
