import time
import paho.mqtt.client as mqtt

BROKER_IP   = "192.168.1.33"  
BROKER_PORT = 1883


def main():
    client = mqtt.Client(client_id="publisher_client")
    client.connect(BROKER_IP, BROKER_PORT, keepalive=60)
    client.loop_start()

    try:
        i = 0
        while True:
            message = f"Hello EMQX! Message #{i}"
            # Publish lên topic "test/topic"
            result = client.publish("test/topic", payload=message, qos=1)
            # Chờ xác nhận
            status = result[0]
            if status == 0:
                print(f"[Publisher] Gửi thành công: {message}")
            else:
                print(f"[Publisher] Gửi thất bại, code={status}")

            i += 1
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n[Publisher] Đang đóng kết nối...")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
