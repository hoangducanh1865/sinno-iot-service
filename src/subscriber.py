import time
import paho.mqtt.client as mqtt

BROKER_IP   = "192.168.1.33" 
BROKER_PORT = 1883


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[Subscriber] Kết nối tới Broker thành công")
        # Subscribe vào topic "test/topic"
        client.subscribe("test/topic")
    else:
        print(f"[Subscriber] Kết nối lỗi, mã lỗi={rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    print(f"[Subscriber] Nhận message trên topic '{msg.topic}': {payload}")

def main():
    client = mqtt.Client(client_id="subscriber_client")
    client.on_connect = on_connect
    client.on_message = on_message

    print(f"[Subscriber] Đang kết nối tới {BROKER_IP}:{BROKER_PORT} ...")
    client.connect(BROKER_IP, BROKER_PORT, keepalive=60)
    client.loop_forever()

if __name__ == "__main__":
    main()
