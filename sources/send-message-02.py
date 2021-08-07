######################################################################################
# This sample is to send a message to Azure IoT Hub using Azure IoT Device Python SDK
# v0.2
# by tz
######################################################################################

import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import json

telemetry = {
    "temperature": 25.78,
    "humidity": 0.65
    }

async def main():
    # Set the connection string
    cs = 'HostName=iothub-0707.azure-devices.net;DeviceId=RPi4-01;SharedAccessKey=INh/Wkg2yM/5eInqqbEEKb+84WgcKYkLmwyeBTWknxo='

    # Create instance of the device client using the connection string
    client = IoTHubDeviceClient.create_from_connection_string(cs)

    # Connect the device client.
    await client.connect()

    # define a send_test_message method
    async def send_test_message():
        print("Sending message ... ")
        msg = Message(json.dumps(telemetry))
        await client.send_message(msg)
        print("Successfully sent message.")

    # send message
    await send_test_message()

    # Finally, shut down the client
    await client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
