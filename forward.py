from telethon import TelegramClient, events
import asyncio

# Your group IDs
Id_Group1 = -1001324987720
Id_Group2 = -1001218506395
Id_Group3 = -1001370181700

# Your API credentials
api_id = '20796854'
api_hash = '26b5566d9211aae142762032996ca30e'

# Initialize the Telethon client
client = TelegramClient('none', api_id, api_hash)

my_list=[]
# Event handler
@client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id
    message_text = event.raw_text.lower()  # Convert the message to lowercase

    # Check if the message has any media (images, videos, documents)
    if not event.media:
        # No media found, proceed with forwarding
        if "free signal" not in message_text and "venturefx signals" in message_text:  # Check for lowercase occurrence
            modified_text = event.raw_text.replace("venturefx signals ©", "J Trading Ltd Signals ©")
            modified_text = modified_text.replace("VENTUREFX SIGNALS ©", "J Trading Ltd Signals ©")

            # Split the modified text into lines
            lines = modified_text.split('\n')

            # Add the separator line after each line
            separator = "||||||||||||||||||||||||||||||||||"
            modified_lines = [line + '\n' + separator for line in lines]

            # Join the modified lines back together
            final_modified_text = '\n'.join(modified_lines)
            
            await client.send_message(Id_Group2, final_modified_text)
            #await client.send_message(Id_Group3, final_modified_text)
       # elif "free signal" in message_text and "venturefx signals" in message_text:
        #    modified_text = event.raw_text.replace("venturefx signals ©", "J Trading Ltd Signals ©")
         #   modified_text = modified_text.replace("VENTUREFX SIGNALS ©", "J Trading Ltd Signals ©")

            # Split the modified text into lines
          #  lines = modified_text.split('\n')

            # Add the separator line after each line
           # separator = "||||||||||||||||||||||||||||||||||"
           # modified_lines = [line + '\n' + separator for line in lines]

            # Join the modified lines back together
           # final_modified_text = '\n'.join(modified_lines)
            
           # await client.send_message(Id_Group3, final_modified_text)
       # elif "free signal hit" in message_text:
        #    modified_text = event.raw_text.replace("venturefx signals ©", "J Trading Ltd Signals ©")
         #   modified_text = modified_text.replace("VENTUREFX SIGNALS ©", "J Trading Ltd Signals ©")

          #  lines = modified_text.split('\n')
           # sep = "|||||||||||||||||||||||||||||||||||||||"
           # mod_lines = [line + '\n' + sep for line in lines]

           # fin_mod_lines = '\n'.join(mod_lines)
           # await client.send_message(Id_Group3, fin_mod_lines)
        elif any(date_phrase in message_text for date_phrase in ["( 01 jan. )", "( 02 jan. )", "( 03 jan. )", "( 04 jan. )", "( 05 jan. )", "( 06 jan. )", "( 07 jan. )", "( 08 jan. )", "( 09 jan. )", "( 10 jan. )", "( 11 jan. )", "( 12 jan. )", "( 13 jan. )", "( 14 jan. )", "( 15 jan. )", "( 16 jan. )", "( 17 jan. )", "( 18 jan. )", "( 19 jan. )", "( 20 jan. )", "( 21 jan. )", "( 22 jan. )", "( 23 jan. )", "( 24 jan. )", "( 25 jan. )", "( 26 jan. )", "( 27 jan. )", "( 28 jan. )", "( 29 jan. )", "( 30 jan. )", "( 31 jan. )", "( 01 feb. )", "( 02 feb. )", "( 03 feb. )", "( 04 feb. )", "( 05 feb. )", "( 06 feb. )", "( 07 feb. )", "( 08 feb. )", "( 09 feb. )", "( 10 feb. )", "( 11 feb. )", "( 12 feb. )", "( 13 feb. )", "( 14 feb. )", "( 15 feb. )", "( 16 feb. )", "( 17 feb. )", "( 18 feb. )", "( 19 feb. )", "( 20 feb. )", "( 21 feb. )", "( 22 feb. )", "( 23 feb. )", "( 24 feb. )", "( 25 feb. )", "( 26 feb. )", "( 27 feb. )", "( 28 feb. )", "( 29 feb. )" , "( 01 mar. )", "( 02 mar. )", "( 03 mar. )", "( 04 mar. )", "( 05 mar. )", "( 06 mar. )", "( 07 mar. )", "( 08 mar. )", "( 09 mar. )", "( 10 mar. )", "( 11 mar. )", "( 12 mar. )", "( 13 mar. )", "( 14 mar. )", "( 15 mar. )", "( 16 mar. )", "( 17 mar. )", "( 18 mar. )", "( 19 mar. )", "( 20 mar. )", "( 21 mar. )", "( 22 mar. )", "( 23 mar. )", "( 24 mar. )", "( 25 mar. )", "( 26 mar. )", "( 27 mar. )", "( 28 mar. )", "( 29 mar. )", "( 30 mar. )", "( 31 mar. )", "( 01 apr. )", "( 02 apr. )", "( 03 apr. )", "( 04 apr. )", "( 05 apr. )", "( 06 apr. )", "( 07 apr. )", "( 08 apr. )", "( 09 apr. )", "( 10 apr. )", "( 11 apr. )", "( 12 apr. )", "( 13 apr. )", "( 14 apr. )", "( 15 apr. )", "( 16 apr. )", "( 17 apr. )", "( 18 apr. )", "( 19 apr. )", "( 20 apr. )", "( 21 apr. )", "( 22 apr. )", "( 23 apr. )", "( 24 apr. )", "( 25 apr. )", "( 26 apr. )", "( 27 apr. )", "( 28 apr. )", "( 29 apr. )", "( 30 apr. )", "( 01 may. )", "( 02 may. )", "( 03 may. )", "( 04 may. )", "( 05 may. )", "( 06 may. )", "( 07 may. )", "( 08 may. )", "( 09 may. )", "( 10 may. )", "( 11 may. )", "( 12 may. )", "( 13 may. )", "( 14 may. )", "( 15 may. )", "( 16 may. )", "( 17 may. )", "( 18 may. )", "( 19 may. )", "( 20 may. )", "( 21 may. )", "( 22 may. )", "( 23 may. )", "( 24 may. )", "( 25 may. )", "( 26 may. )", "( 27 may. )", "( 28 may. )", "( 29 may. )", "( 30 may. )", "( 31 may. )", "( 01 jun. )", "( 02 jun. )", "( 03 jun. )", "( 04 jun. )", "( 05 jun. )", "( 06 jun. )", "( 07 jun. )", "( 08 jun. )", "( 09 jun. )", "( 10 jun. )", "( 11 jun. )", "( 12 jun. )", "( 13 jun. )", "( 14 jun. )", "( 15 jun. )", "( 16 jun. )", "( 17 jun. )", "( 18 jun. )", "( 19 jun. )", "( 20 jun. )", "( 21 jun. )", "( 22 jun. )", "( 23 jun. )", "( 24 jun. )", "( 25 jun. )", "( 26 jun. )", "( 27 jun. )", "( 28 jun. )", "( 29 jun. )", "( 30 jun. )", "( 01 jul. )", "( 02 jul. )", "( 03 jul. )", "( 04 jul. )", "( 05 jul. )", "( 06 jul. )", "( 07 jul. )", "( 08 jul. )", "( 09 jul. )", "( 10 jul. )", "( 11 jul. )", "( 12 jul. )", "( 13 jul. )", "( 14 jul. )", "( 15 jul. )", "( 16 jul. )", "( 17 jul. )", "( 18 jul. )", "( 19 jul. )", "( 20 jul. )", "( 21 jul. )", "( 22 jul. )", "( 23 jul. )", "( 24 jul. )", "( 25 jul. )", "( 26 jul. )", "( 27 jul. )", "( 28 jul. )", "( 29 jul. )", "( 30 jul. )", "( 31 jul. )", "( 01 aug. )", "( 02 aug. )", "( 03 aug. )", "( 04 aug. )", "( 05 aug. )", "( 06 aug. )", "( 07 aug. )", "( 08 aug. )", "( 09 aug. )", "( 10 aug. )", "( 11 aug. )", "( 12 aug. )", "( 13 aug. )", "( 14 aug. )", "( 15 aug. )", "( 16 aug. )", "( 17 aug. )", "( 18 aug. )", "( 19 aug. )", "( 20 aug. )", "( 21 aug. )", "( 22 aug. )", "( 23 aug. )", "( 24 aug. )", "( 25 aug. )", "( 26 aug. )", "( 27 aug. )", "( 28 aug. )", "( 29 aug. )", "( 30 aug. )", "( 31 aug. )", "( 01 sep. )", "( 02 sep. )", "( 03 sep. )", "( 04 sep. )", "( 05 sep. )", "( 06 sep. )", "( 07 sep. )", "( 08 sep. )", "( 09 sep. )", "( 10 sep. )", "( 11 sep. )", "( 12 sep. )", "( 13 sep. )", "( 14 sep. )", "( 15 sep. )", "( 16 sep. )", "( 17 sep. )", "( 18 sep. )", "( 19 sep. )", "( 20 sep. )", "( 21 sep. )", "( 22 sep. )", "( 23 sep. )", "( 24 sep. )", "( 25 sep. )", "( 26 sep. )", "( 27 sep. )", "( 28 sep. )", "( 29 sep. )", "( 30 sep. )", "( 01 oct. )", "( 02 oct. )", "( 03 oct. )", "( 04 oct. )", "( 05 oct. )", "( 06 oct. )", "( 07 oct. )", "( 08 oct. )", "( 09 oct. )", "( 10 oct. )", "( 11 oct. )", "( 12 oct. )", "( 13 oct. )", "( 14 oct. )", "( 15 oct. )", "( 16 oct. )", "( 17 oct. )", "( 18 oct. )", "( 19 oct. )", "( 20 oct. )", "( 21 oct. )", "( 22 oct. )", "( 23 oct. )", "( 24 oct. )", "( 25 oct. )", "( 26 oct. )", "( 27 oct. )", "( 28 oct. )", "( 29 oct. )", "( 30 oct. )", "( 31 oct. )", "( 01 nov. )", "( 02 nov. )", "( 03 nov. )", "( 04 nov. )", "( 05 nov. )", "( 06 nov. )", "( 07 nov. )", "( 08 nov. )", "( 09 nov. )", "( 10 nov. )", "( 11 nov. )", "( 12 nov. )", "( 13 nov. )", "( 14 nov. )", "( 15 nov. )", "( 16 nov. )", "( 17 nov. )", "( 18 nov. )", "( 19 nov. )", "( 20 nov. )", "( 21 nov. )", "( 22 nov. )", "( 23 nov. )", "( 24 nov. )", "( 25 nov. )", "( 26 nov. )", "( 27 nov. )", "( 28 nov. )", "( 29 nov. )", "( 30 nov. )", "( 01 dec. )", "( 02 dec. )", "( 03 dec. )", "( 04 dec. )", "( 05 dec. )", "( 06 dec. )", "( 07 dec. )", "( 08 dec. )", "( 09 dec. )", "( 10 dec. )", "( 11 dec. )", "( 12 dec. )", "( 13 dec. )", "( 14 dec. )", "( 15 dec. )", "( 16 dec. )", "( 17 dec. )", "( 18 dec. )", "( 19 dec. )", "( 20 dec. )", "( 21 dec. )", "( 22 dec. )", "( 23 dec. )", "( 24 dec. )", "( 25 dec. )", "( 26 dec. )", "( 27 dec. )", "( 28 dec. )", "( 29 dec. )", "( 30 dec. )", "( 31 dec. )" ]):
            if message_text in my_list:
                pass
            else:
                my_list.append(message_text)
                await client.send_message(Id_Group2, event.raw_text)
                await client.send_message(Id_Group3, event.raw_text)
            


# Start the client and run until disconnected
client.start()
client.run_until_disconnected()
