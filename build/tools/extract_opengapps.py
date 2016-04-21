#!/usr/bin/env python
import os, sys
import shutil

# List of opengapps apks ('super' build variant) following the format: (Location, opengapps_appname, build_arch, dpis, priv, appname)
# Currently excluded from the lists below: gFi, speech, indic, pinyin, zhuyin, japanese, korean, street
COMMON_APKS = (
	('Core', 'configupdater', 'all', ('nodpi', ), 'priv-app', 'ConfigUpdater'),
	('Core', 'gmscore', 'arm', ('nodpi', '240', '320', '480'), 'priv-app', 'PrebuiltGmsCore'),
	('Core', 'googlebackuptransport', 'all', ('nodpi', ), 'priv-app', 'GoogleBackupTransport'),
	('Core', 'googlecontactssync', 'all', ('nodpi', ), 'app', 'GoogleContactsSyncAdapter'),
	('Core', 'googlefeedback', 'all', ('nodpi', ), 'priv-app', 'GoogleFeedback'),
	('Core', 'googleonetimeinitializer', 'all', ('nodpi', ), 'priv-app', 'GoogleOneTimeInitializer'),
	('Core', 'googlepartnersetup', 'all', ('nodpi', ), 'priv-app', 'GooglePartnerSetup'),
	('Core', 'gsfcore', 'all', ('nodpi', ), 'priv-app', 'GoogleServicesFramework'),
	('Core', 'gsflogin', 'all', ('nodpi', ), 'priv-app', 'GoogleLoginService'),
	('Core', 'vending', 'all', ('nodpi', ), 'priv-app', 'Phonesky'),
#	('GApps', 'androidforwork', ('nodpi',), 'priv-app', 'AndroidForWork'),
	('GApps', 'androidpay', 'arm', ('nodpi', '480', '640',), 'app', 'Wallet'),
	('GApps', 'books', 'all', ('nodpi', ), 'app', 'Books'),
	('GApps', 'calculatorgoogle', 'all', ('nodpi', ), 'app', 'CalculatorGoogle'),
	('GApps', 'calendargoogle', 'all', ('nodpi', ), 'app', 'CalendarGooglePrebuilt'),
	('GApps', 'calsync', 'all', ('nodpi', ), 'app', 'GoogleCalendarSyncAdapter'),
	('GApps', 'cameragoogle', 'arm', ('nodpi', ), 'app', 'GoogleCamera'),
	('GApps', 'chrome', 'arm', ('nodpi', ), 'app', 'Chrome'),
	('GApps', 'clockgoogle', 'all', ('nodpi', ), 'app', 'PrebuiltDeskClockGoogle'),
	('GApps', 'cloudprint', 'all', ('nodpi', ), 'app', 'CloudPrint2'),
	('GApps', 'contactsgoogle', 'all', ('nodpi', ), 'priv-app', 'GoogleContacts'),
	('GApps', 'dialergoogle', 'all', ('nodpi', ), 'priv-app', 'GoogleDialer'),
	('GApps', 'dmagent', 'all', ('nodpi', ), 'app', 'DMAgent'),
	('GApps', 'docs', 'arm', ('nodpi', '160', '240', '320', '480', '640',), 'app', 'EditorsDocs'),
	('GApps', 'drive', 'arm', ('nodpi', '160', '240', '320', '480', '640',), 'app', 'Drive'),
	('GApps', 'ears', 'all', ('nodpi', ), 'app', 'GoogleEars'),
	('GApps', 'earth', 'arm', ('nodpi', '120-160', '213-240', '320', '480',), 'app', 'GoogleEarth'),
	('GApps', 'exchangegoogle', 'all', ('nodpi', ), 'app', 'PrebuiltExchange3Google'),
	('GApps', 'faceunlock', 'all', ('nodpi', ), 'app', 'FaceLock'),
	('GApps', 'fitness', 'all', ('nodpi', '160', '240', '320', '480', '640',), 'app', 'FitnessPrebuilt'),
	('GApps', 'gcs', 'all', ('nodpi', ), 'priv-app', 'GCS'),
	('GApps', 'gmail', 'all', ('nodpi', ), 'app', 'PrebuiltGmail'),
	('GApps', 'googlenow', 'all', ('nodpi', ), 'app', 'GoogleHome'),
	('GApps', 'googleplus', 'arm', ('nodpi', '480',), 'app', 'PlusOne'),
	('GApps', 'googletts', 'arm', ('nodpi', ), 'app', 'GoogleTTS'),
	('GApps', 'hangouts', 'arm', ('160', '213-240', '320', '400-420', '560-640', ), 'app', 'Hangouts'),
	('GApps', 'keep', 'arm', ('nodpi', ), 'app', 'PrebuiltKeep'),
	('GApps', 'keyboardgoogle', 'arm', ('nodpi', ), 'app', 'LatinImeGoogle'),
	('GApps', 'maps', 'arm', ('213-240', '320', '400-480', '560-640', ), 'app', 'Maps'),
	('GApps', 'messenger', 'arm', ('nodpi', '160', '240', '320', '480', '640', ), 'app', 'PrebuiltBugle'),
	('GApps', 'movies', 'arm', ('nodpi', ), 'app', 'Videos'),
	('GApps', 'music', 'all', ('nodpi', ), 'app', 'Music2'),
	('GApps', 'newsstand', 'all', ('nodpi', ), 'app', 'Newsstand'),
	('GApps', 'newswidget', 'all', ('nodpi', ), 'app', 'PrebuiltNewsWeather'),
	('GApps', 'packageinstallergoogle', 'all', ('nodpi', ), 'priv-app', 'GooglePackageInstaller'),
	('GApps', 'photos', 'arm', ('nodpi', '160', '240', '320', '400-420-480-560', ), 'app', 'Photos'),
	('GApps', 'playgames', 'arm', ('nodpi', '160', '240', '320', '480', ), 'app', 'PlayGames'),
	('GApps', 'search', 'arm', ('nodpi', '160', '240', '320', ), 'priv-app', 'Velvet'),
	('GApps', 'sheets', 'arm', ('nodpi', '160', '240', '320', '480', '640',), 'app', 'EditorsSheets'),
	('GApps', 'slides', 'arm', ('nodpi', '160', '240', '320', '480', '640',), 'app', 'EditorsSlides'),
	('GApps', 'taggoogle', 'all', ('nodpi', ), 'priv-app', 'TagGoogle'),
	('GApps', 'talkback', 'all', ('nodpi', ), 'app', 'talkback'),
	('GApps', 'translate', 'arm', ('nodpi', ), 'app', 'TranslatePrebuilt'),
	('GApps', 'webviewgoogle', 'arm', ('nodpi', ), 'app', 'WebViewGoogle'),
	('GApps', 'youtube', 'arm', ('nodpi', '160', '240', '320', '480', ), 'app', 'YouTube'),
)
OCCAM_APKS = (
	('Core', 'setupwizarddefault', 'all', ('nodpi', ), 'priv-app', 'SetupWizard'),
)
NAKASIG_APKS = (
	('Core', 'setupwizardtablet', 'all', ('nodpi', ), 'priv-app', 'SetupWizard'),
)

# Type the following command in the opengapps build directory: find . -name *.xml
# Only results of command above starting with ./Core or ./GApps
# List vary with build variant
OPENGAPPS_DATA = [
    './Core/defaultetc-all/common/etc/sysconfig/google.xml',
    './Core/defaultetc-all/common/etc/sysconfig/google_build.xml',
    './Core/defaultetc-all/common/etc/sysconfig/whitelist_com.android.omadm.service.xml',
    './Core/defaultetc-all/common/etc/preferred-apps/google.xml',
    './Core/defaultframework-all/common/etc/permissions/com.google.android.maps.xml',
    './Core/defaultframework-all/common/etc/permissions/com.google.android.media.effects.xml',
    './Core/defaultframework-all/common/etc/permissions/com.google.widevine.software.drm.xml',
    './GApps/dialerframework-all/common/etc/permissions/com.google.android.dialer.support.xml',
    './GApps/cameragoogle-all/common/etc/permissions/com.google.android.camera.experimental2015.xml' ]
# Type the following command in the opengapps build directory: find . -name *.bin
# Only results of command above starting with ./Core or ./GApps
# List vary with build variant
OPENGAPPS_FACELOCK_6 = [
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/multi_pose_face_landmark_detectors.8/left_eye-y0-yi45-p0-pi45-r0-ri20.lg_32-tree7-wmd.bin',
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/multi_pose_face_landmark_detectors.8/landmark_group_meta_data.bin',
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/multi_pose_face_landmark_detectors.8/nose_base-y0-yi45-p0-pi45-r0-ri20.lg_32-tree7-wmd.bin',
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/multi_pose_face_landmark_detectors.8/right_eye-y0-yi45-p0-pi45-r0-ri20.lg_32-3-tree7-wmd.bin',
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/head-y0-yi45-p0-pi45-r0-ri30.4a-v24-tree7-2-wmd.bin',
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/pose-r.8.1.bin',
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/pose-y-r.8.1.bin',
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/head-y0-yi45-p0-pi45-rn30-ri30.5-v24-tree7-2-wmd.bin',
    './GApps/faceunlock-all/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/head-y0-yi45-p0-pi45-rp30-ri30.5-v24-tree7-2-wmd.bin' ]
OPENGAPPS_FACELOCK_5 = [
    './GApps/faceunlock-all/common/vendor/pittpatt/models/recognition/face.face.y0-y0-71-N-tree_7-wmd.bin' ]
# Type the following command in the opengapps build directory: find . -name *.so
# Only results of command above starting with ./Core or ./GApps
# List vary with build variant
OPENGAPPS_FACELOCK_2 = [
    './GApps/faceunlock-arm/common/vendor/lib/libfrsdk.so',
    './GApps/faceunlock-arm/common/lib/libfacelock_jni.so',
    './GApps/facedetect-arm/common/lib/libfilterpack_facedetect.so' ]
# Type the following command in the opengapps build directory: find . -name *.jar
# Only results of command above starting with ./Core or ./GApps
# List vary with build variant
OPENGAPPS_JAR = [
    './Core/defaultframework-all/common/framework/com.google.widevine.software.drm.jar',
    './Core/defaultframework-all/common/framework/com.google.android.media.effects.jar',
    './Core/defaultframework-all/common/framework/com.google.android.maps.jar',
    './GApps/dialerframework-all/common/framework/com.google.android.dialer.support.jar',
    './GApps/cameragoogle-all/common/framework/com.google.android.camera.experimental2015.jar' ]
# Type the following command in the opengapps build directory: find . -name *.so
# Only results of command above starting with ./Core or ./GApps
# List vary with build variant
OPENGAPPS_LIB = [
    './Optional/swypelibs-arm/common/lib/libjni_latinimegoogle.so', 
    './Optional/swypelibs-arm/common/lib/libjni_keyboarddecoder.so' ]

# Required android tools
AAPT = 'aapt'

# vendor/google repo directory structure
APPS_DIR = 'apps'
DATA_DIR = 'data'
ETC_DIR = 'etc'
PERMISSIONS_DIR = 'permissions'
PREFERRED_APPS_DIR = 'preferred-apps'
SYSCONFIG_DIR = 'sysconfig'
FRAMEWORK_DIR = 'framework'
LIB_DIR = 'lib'
FACELOCK_DIR = 'facelock'
FACELOCK_VENDOR_DIR = 'vendor'
PITTPATT_DIR = 'pittpatt'
MODELS_DIR = 'models'
DETECTION_DIR = 'detection'
MULTIPOSE_DIR = "multi_pose_face_landmark_detectors.8"
YAWROLL_DIR = 'yaw_roll_face_detectors.7.1'
RECOGNITION_DIR = 'recognition'

def checkPrerequisites():
    tools = AAPT, 
    for tool in tools:
        if os.system('which %s'%tool):
            print 'Please install %s in your PATH' %tool
            sys.exit(1)
    return True

def checkOpengappsBuildDir(path):
    return os.path.exists(os.path.join(path, 'Core')) and os.path.exists(os.path.join(path, 'GApps')) and os.path.exists(os.path.join(path, 'Optional'))

def prepareDirectories():
    VENDOR_DIR = os.path.join(os.path.dirname(__file__), '..', '..')
    def makedirs(path):
        if os.path.isdir(path):
            return
        os.makedirs(path)

    for dirname in (APPS_DIR, DATA_DIR, os.path.join(DATA_DIR, ETC_DIR),
                    os.path.join(DATA_DIR, ETC_DIR, PERMISSIONS_DIR),
                    os.path.join(DATA_DIR, ETC_DIR, PREFERRED_APPS_DIR),
                    os.path.join(DATA_DIR, ETC_DIR, SYSCONFIG_DIR),
                    FRAMEWORK_DIR, 
                    LIB_DIR,
                    os.path.join(LIB_DIR,FACELOCK_DIR),
                    os.path.join(LIB_DIR,FACELOCK_DIR,FACELOCK_VENDOR_DIR),
                    os.path.join(LIB_DIR,FACELOCK_DIR,FACELOCK_VENDOR_DIR,PITTPATT_DIR),
                    os.path.join(LIB_DIR,FACELOCK_DIR,FACELOCK_VENDOR_DIR,PITTPATT_DIR,MODELS_DIR),
                    os.path.join(LIB_DIR,FACELOCK_DIR,FACELOCK_VENDOR_DIR,PITTPATT_DIR,MODELS_DIR,DETECTION_DIR),
                    os.path.join(LIB_DIR,FACELOCK_DIR,FACELOCK_VENDOR_DIR,PITTPATT_DIR,MODELS_DIR,DETECTION_DIR,MULTIPOSE_DIR),
                    os.path.join(LIB_DIR,FACELOCK_DIR,FACELOCK_VENDOR_DIR,PITTPATT_DIR,MODELS_DIR,DETECTION_DIR,YAWROLL_DIR),
                    os.path.join(LIB_DIR,FACELOCK_DIR,FACELOCK_VENDOR_DIR,PITTPATT_DIR,MODELS_DIR,RECOGNITION_DIR),
                    os.path.join(LIB_DIR,FACELOCK_DIR,LIB_DIR),):
        makedirs(os.path.join(VENDOR_DIR, dirname))
    return VENDOR_DIR

def apk_rename(filename):
    cmd = 'aapt d badging ' + filename
    attrs = {}
    p = os.popen(cmd)
    for line in p:
        line = line[:-1]
        line = line.decode('utf-8')
        if line.startswith('package: '):
            line = line.split(None, 1)[1]
            line = line.strip()
            while line:
                k, line = line.split('=', 1)
                _, line = line.split("'", 1)
                v, line = line.split("'", 1)
                attrs[k] = v
                line = line.strip()
            break
    newname = attrs['name'] + '.apk'
    newname = os.path.join(vendor_dir, APPS_DIR, newname)
    if filename != newname:
        print('rename %s => %s'%(filename, newname))
        if os.access(newname, os.F_OK):
            os.unlink(newname)
        os.rename(filename, newname)

def dpi_selection(device_name, dpis):
    if device_name == 'occam':
        optimal_dpi = ''
        for dpi in dpis:
            if dpi == 'nodpi':
                optimal_dpi = 'nodpi'
            elif dpi == '320':
                optimal_dpi = '320'
                break
    if device_name == 'nakasig':
        optimal_dpi = ''
        for dpi in dpis:
            if dpi == 'nodpi':
                optimal_dpi = 'nodpi'
            elif dpi == '213':
                optimal_dpi = '213'
                break
            elif dpi == '213-240':
                optimal_dpi = '213-240'
                break
            elif dpi == '240':
                optimal_dpi = '240'
                break
    return optimal_dpi

def copy_opengapps_apk(apks):
    for apk in apks:
        location, opengapps_appname, build_arch, dpis, system_dir, appname = apk
        device_dpi = dpi_selection(device_name, dpis)
        if device_dpi != '':
            src = os.path.join(opengapps_path, location, opengapps_appname + '-' + build_arch, device_dpi, system_dir, appname, appname + '.apk')
            dst = os.path.join(vendor_dir, APPS_DIR, appname + '.apk')
            try:
                print 'Copying %s...' %src
                shutil.copy(src, dst)
                apk_rename(dst)
            except:
                print 'ERROR: could not copy/rename %s to %s' % (src, dst)
        else:
            print 'WARNING: %s does not have a valid dpi for %s device and could not be copied to google/vendor repo' % (appname, device_name)

def copy_opengapps_files(build_path, opengapps_files, dst_dir, common_dir_depth):
    result = []
    for i in range(common_dir_depth):
        result.append('')
    for opengapps_file in opengapps_files:
        file_to_copy = opengapps_file
        for i in range(common_dir_depth):
            split_path = os.path.split(opengapps_file)
            result[common_dir_depth - 1 - i] = split_path[1]
            opengapps_file = split_path[0]
        inpfile = os.path.join(build_path, file_to_copy)
        outfile = os.path.join(dst_dir, *result)
        try:
            print 'Copying %s...' % (inpfile)
            shutil.copy(inpfile, outfile)
        except:
            print 'ERROR: could not copy %s to %s' % (inpfile, outfile)

if __name__ == '__main__':
    # Check usage
    if len(sys.argv) != 3:
        print 'Usage: %s device_name opengapps_build_path' % sys.argv[0]
        print 'Note: %s currently works only with the following devices: occam or nakasig' % sys.argv[0]
        sys.exit(1)
    
    # Check device input by user is supported
    device_name = sys.argv[1]
    if device_name != 'occam' and device_name != 'nakasig':
        print '%s currently works only with the following devices: occam or nakasig' % sys.argv[0]
        sys.exit(1)
    
    # Check opengapps directory input by user is valid
    opengapps_path = sys.argv[2]
    if not checkOpengappsBuildDir(opengapps_path):
        print 'Error: %s is not a valid openGapps build directory.' % opengapps_path
        sys.exit(1)

    # Check prerequisites are met (aapt is available)
    checkPrerequisites()
    
    # Create necessary directories in vendor/google repo
    vendor_dir = prepareDirectories()
    
    # Copy opengapps apks to vendor/google/apps repo
    copy_opengapps_apk(COMMON_APKS)
    if device_name == 'occam':
        copy_opengapps_apk(OCCAM_APKS)
    elif device_name == 'nakasig':
        copy_opengapps_apk(NAKASIG_APKS)
    else:
        print 'Device %s not supported' %device_name
    
    # Copy xml files to vendor/google repo
    dst = os.path.join(vendor_dir, DATA_DIR)
    copy_opengapps_files(opengapps_path, OPENGAPPS_DATA, dst, 3)
    
    # Copy facelock binary and so files to vendor/google repo
    dst = os.path.join(vendor_dir, LIB_DIR, 'facelock')
    copy_opengapps_files(opengapps_path, OPENGAPPS_FACELOCK_6, dst, 6)
    copy_opengapps_files(opengapps_path, OPENGAPPS_FACELOCK_5, dst, 5)
    copy_opengapps_files(opengapps_path, OPENGAPPS_FACELOCK_2, dst, 2)
    
    # Copy jar files to vendor/google repo
    dst = vendor_dir
    copy_opengapps_files(opengapps_path, OPENGAPPS_JAR, dst, 2)
    
    # Copy app libraries files to vendor/google repo
    dst = os.path.join(vendor_dir, APPS_DIR)
    copy_opengapps_files(opengapps_path, OPENGAPPS_LIB, dst, 1)
