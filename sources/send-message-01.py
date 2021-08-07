######################################################################################
# This sample is to send a message to Azure IoT Hub using Azure IoT Device Python SDK
# v0.1
# by tz
######################################################################################

import asyncio
from azure.iot.device.aio import IoTHubDeviceClient


async def main():
    # Set the connection string
    cs = 'HostName=iothub-0707.azure-devices.net;DeviceId=RPi4-01;SharedAccessKey=INh/Wkg2yM/5eInqqbEEKb+84WgcKYkLmwyeBTWknxo='

    # Create instance of the device client using the connection string
    client = IoTHubDeviceClient.create_from_connection_string(cs)

    # Connect the device client.
    await client.connect()

    # Send a single message
    print("Sending message...")
    await client.send_message("Hello from tz!")
    print("Message successfully sent!")

    # Finally, shut down the client
    await client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

