import grpc
import p_greet_pb2
import p_greet_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50055") as channel:
        stub = p_greet_pb2_grpc.P_GREETERStub(channel)
        payload = {
            "name": "Siraj",
            "greeting": "Molo",
        }
        greet_request = p_greet_pb2.GreetRequest(**payload)
        greet_response = stub.Greet(greet_request)
        print("Response from Server")
        print(greet_response)
        
if __name__ == "__main__":
    run()
        