import asyncio
import argparse
import subprocess
import sys
import os.path
import yaml
import nest_asyncio

nest_asyncio.apply()


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="the profile pic you want to change to")
    args = parser.parse_args() 
    print(args.image)
    
    with open('config.yaml', 'r') as f:
        user_logins = yaml.safe_load(f)['accounts']
    
    subprocess.call([sys.executable, os.path.join("platforms", "discord_pfp.py"), user_logins['discord']['token'], user_logins['discord']['password'], args.image], stderr=subprocess.DEVNULL)
    

if __name__ == '__main__':
    asyncio.run(main())

