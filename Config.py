#imports
import os

# The android version that we're targeting this application to run
TARGET_ANDROID_VERSION = 11

# Possible Values are  ['fetch', 'build', 'zip']
# 'fetch' will pull the files from the device
# 'build' will pull the files from the device and zip them
# 'zip' will create the package from existing files
APPLICATION_RUN_TYPE = "zip"

# Fetch Package should always be super set of Build Package
# Possible Values are ['core', 'basic', 'omni', 'macro', 'stock', 'full', 'ultra', 'addons', 'addonsets']
FETCH_PACKAGE = "full"
BUILD_PACKAGE_LIST = ['core', 'basic', 'omni', 'macro', 'stock', 'full', 'addons', 'addonsets']

if TARGET_ANDROID_VERSION == 10:
    BUILD_PACKAGE_LIST.append("go")

# Send the zip to device after creation, Possible values are True and False
SEND_ZIP_DEVICE = True

# Setup wizard comes with two types. Google Setup Wizard and Pixel Setup Wizard, none will skip it
SETUP_WIZARD = "pixel"  # Possible values are ['google', 'pixel', 'none']

# This will help fetch the files which requires root access such as overlay files
ADB_ROOT_ENABLED = False

# This will create a Debloater Zip
CREATE_DEBLOATER_ZIP = True

# This will allow the program to sign the zip
SIGN_ZIP = True

# Bot's Token
TOKEN = os.environ.get("BOT_TOKEN")
url = f'https://api.telegram.org/bot{TOKEN}/'

# When Fresh Build is True, the installer will freshly build the zip (Comparatively Slower)
# When Fresh Build is False, the installer picks up existing zip and builds gapps package (Faster)
FRESH_BUILD = True
