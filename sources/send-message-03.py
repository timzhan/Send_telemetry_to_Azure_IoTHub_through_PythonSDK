######################################################################################
# This sample is to send simulated telemetry to Azure IoT Hub using Azure IoT Device Python SDK
# v0.3
# by tz
######################################################################################

import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import json
import random as rnd

times = 3

# Write a method to simulate telemetry
def simulate_telemetry():
    t = round(rnd.uniform(10.0, 35.0), 2)
    h = round(rnd.uniform(0.1, 0.8),2)

    telemetry = {
        "temperature": t,
        "humidity": h
        }

    return telemetry

async def main():
    # Set the connection string
    cs = 'HostName=iothub-0707.azure-devices.net;DeviceId=RPi4-01;SharedAccessKey=INh/Wkg2yM/5eInqqbEEKb+84WgcKYkLmwyeBTWknxo='

    # Create instance of the device client using the connection string
    client = IoTHubDeviceClient.create_from_connection_string(cs)

    # Connect the device client.
    await client.connect()

    # define a send_test_message method
    async def send_test_message(n):
        for i in range(1, n + 1):
            print("Sending message # " + str(i))
            msg = Message(json.dumps(simulate_telemetry()))
            await client.send_message(msg)
            print("Successfully sent message #" + str(i))

    # send `specified times` messages in parallel
    await send_test_message(times)

    # Finally, shut down the client
    await client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

