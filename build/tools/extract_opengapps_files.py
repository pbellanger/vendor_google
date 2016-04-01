#!/usr/bin/env python
import os, sys
#import errno
#import glob
#import re
import shutil
#import struct
#import subprocess
#import zipfile

# Required android tools
AAPT = 'aapt'
ZIPALIGN = 'zipalign'

# vendor/google repo directory structure
DATA_DIR = 'data'
ETC_DIR = 'etc'
PERMISSIONS_DIR = 'permissions'
PREFERRED_APPS_DIR = 'preferred-apps'
SYSCONFIG_DIR = 'sysconfig'
FRAMEWORK_DIR = 'framework'
LIB_DIR = 'lib'
APPS_DIR = 'apps'
# OpenGapps build information
ARCH = 'arm'
SDK = '23'
BUILD_VARIANT = 'stock'
OPENGAPPS_DATA = [
    './Core/defaultetc/common/etc/sysconfig/google.xml',
    './Core/defaultetc/common/etc/sysconfig/google_build.xml',
    './Core/defaultetc/common/etc/sysconfig/whitelist_com.android.omadm.service.xml',
    './Core/defaultetc/common/etc/preferred-apps/google.xml',
    './Core/defaultframework/common/etc/permissions/com.google.android.maps.xml',
    './Core/defaultframework/common/etc/permissions/com.google.android.media.effects.xml',
    './Core/defaultframework/common/etc/permissions/com.google.widevine.software.drm.xml',
    './GApps/dialergoogle/common/etc/permissions/com.google.android.dialer.support.xml',
    './GApps/cameragooglelegacy/common/etc/permissions/com.google.android.camera2.xml',
    './GApps/cameragoogle/common/etc/permissions/com.google.android.camera.experimental2015.xml' ]
OPENGAPPS_FACELOCK_6 = [
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/multi_pose_face_landmark_detectors.8/left_eye-y0-yi45-p0-pi45-r0-ri20.lg_32-tree7-wmd.bin',
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/multi_pose_face_landmark_detectors.8/landmark_group_meta_data.bin',
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/multi_pose_face_landmark_detectors.8/nose_base-y0-yi45-p0-pi45-r0-ri20.lg_32-tree7-wmd.bin',
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/multi_pose_face_landmark_detectors.8/right_eye-y0-yi45-p0-pi45-r0-ri20.lg_32-3-tree7-wmd.bin',
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/head-y0-yi45-p0-pi45-r0-ri30.4a-v24-tree7-2-wmd.bin',
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/pose-r.8.1.bin',
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/pose-y-r.8.1.bin',
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/head-y0-yi45-p0-pi45-rn30-ri30.5-v24-tree7-2-wmd.bin',
    './GApps/faceunlock/common/vendor/pittpatt/models/detection/yaw_roll_face_detectors.7.1/head-y0-yi45-p0-pi45-rp30-ri30.5-v24-tree7-2-wmd.bin' ]
OPENGAPPS_FACELOCK_5 = [
    './GApps/faceunlock/common/vendor/pittpatt/models/recognition/face.face.y0-y0-71-N-tree_7-wmd.bin' ]
OPENGAPPS_FACELOCK_2 = [
    './GApps/faceunlock/common/vendor/lib/libfrsdk.so',
    './GApps/faceunlock/common/lib/libfacelock_jni.so',
    './GApps/facedetect/common/lib/libfilterpack_facedetect.so' ]
OPENGAPPS_JAR = [
    './Core/defaultframework/common/framework/com.google.widevine.software.drm.jar',
    './Core/defaultframework/common/framework/com.google.android.media.effects.jar',
    './Core/defaultframework/common/framework/com.google.android.maps.jar',
    './GApps/dialergoogle/common/framework/com.google.android.dialer.support.jar',
    './GApps/cameragooglelegacy/common/framework/com.google.android.camera2.jar',
    './GApps/cameragoogle/common/framework/com.google.android.camera.experimental2015.jar' ]
OPENGAPPS_LIB = [
    './Optional/swypelibs/common/lib/libjni_latinimegoogle.so', 
    './Optional/swypelibs/common/lib/libjni_keyboarddecoder.so' ]
OPENGAPPS_APP = [ './Core/googlecontactssync/nodpi/app/GoogleContactsSyncAdapter/GoogleContactsSyncAdapter.apk', 
    './GApps/books/nodpi/app/Books/Books.apk', 
    './GApps/calculatorgoogle/nodpi/app/CalculatorGoogle/CalculatorGoogle.apk', 
    './GApps/cloudprint/nodpi/app/CloudPrint2/CloudPrint2.apk', 
    './GApps/clockgoogle/nodpi/app/PrebuiltDeskClockGoogle/PrebuiltDeskClockGoogle.apk', 
    './GApps/ears/nodpi/app/GoogleEars/GoogleEars.apk', 
    './GApps/docs/nodpi/app/EditorsDocs/EditorsDocs.apk', 
    './GApps/chrome/nodpi/app/Chrome/Chrome.apk', 
    './GApps/faceunlock/nodpi/app/FaceLock/FaceLock.apk', 
    './GApps/gmail/nodpi/app/PrebuiltGmail/PrebuiltGmail.apk', 
    './GApps/drive/nodpi/app/Drive/Drive.apk', 
    './GApps/webviewgoogle/nodpi/app/WebViewGoogle/WebViewGoogle.apk', 
    './GApps/calendargoogle/nodpi/app/CalendarGooglePrebuilt/CalendarGooglePrebuilt.apk', 
    './GApps/keyboardgoogle/nodpi/app/LatinImeGoogle/LatinImeGoogle.apk', 
    './GApps/youtube/nodpi/app/YouTube/YouTube.apk', 
    './GApps/photos/nodpi/app/Photos/Photos.apk', 
    './GApps/exchangegoogle/nodpi/app/PrebuiltExchange3Google/PrebuiltExchange3Google.apk', 
    './GApps/keep/nodpi/app/PrebuiltKeep/PrebuiltKeep.apk', 
    './GApps/sheets/nodpi/app/EditorsSheets/EditorsSheets.apk', 
    './GApps/fitness/nodpi/app/FitnessPrebuilt/FitnessPrebuilt.apk', 
    './GApps/slides/nodpi/app/EditorsSlides/EditorsSlides.apk', 
    './GApps/playgames/nodpi/app/PlayGames/PlayGames.apk', 
    './GApps/newsstand/nodpi/app/Newsstand/Newsstand.apk', 
    './GApps/googlenow/nodpi/app/GoogleHome/GoogleHome.apk', 
    './GApps/cameragooglelegacy/nodpi/app/GoogleCamera/GoogleCamera.apk', 
    './GApps/talkback/nodpi/app/talkback/talkback.apk', 
    './GApps/music/nodpi/app/Music2/Music2.apk', 
    './GApps/cameragoogle/nodpi/app/GoogleCamera/GoogleCamera.apk', 
    './GApps/googletts/nodpi/app/GoogleTTS/GoogleTTS.apk', 
    './GApps/movies/nodpi/app/Videos/Videos.apk', 
    './GApps/calsync/nodpi/app/GoogleCalendarSyncAdapter/GoogleCalendarSyncAdapter.apk', 
    './GApps/newswidget/nodpi/app/PrebuiltNewsWeather/PrebuiltNewsWeather.apk', 
    './GApps/maps/nodpi/app/Maps/Maps.apk' ]
OPENGAPPS_PRIV_APP = [ './Core/setupwizarddefault/nodpi/priv-app/SetupWizard/SetupWizard.apk', 
    './Core/googleonetimeinitializer/nodpi/priv-app/GoogleOneTimeInitializer/GoogleOneTimeInitializer.apk', 
    './Core/googlepartnersetup/nodpi/priv-app/GooglePartnerSetup/GooglePartnerSetup.apk', 
    './Core/gsflogin/nodpi/priv-app/GoogleLoginService/GoogleLoginService.apk', 
    './Core/vending/nodpi/priv-app/Phonesky/Phonesky.apk', 
    './Core/configupdater/nodpi/priv-app/ConfigUpdater/ConfigUpdater.apk', 
    './Core/gmscore/nodpi/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk', 
    './Core/setupwizardtablet/nodpi/priv-app/SetupWizard/SetupWizard.apk', 
    './Core/googlebackuptransport/nodpi/priv-app/GoogleBackupTransport/GoogleBackupTransport.apk', 
    './Core/googlefeedback/nodpi/priv-app/GoogleFeedback/GoogleFeedback.apk', 
    './Core/gsfcore/nodpi/priv-app/GoogleServicesFramework/GoogleServicesFramework.apk', 
    './GApps/search/nodpi/priv-app/Velvet/Velvet.apk', 
    './GApps/packageinstallergoogle/nodpi/priv-app/GooglePackageInstaller/GooglePackageInstaller.apk', 
    './GApps/taggoogle/nodpi/priv-app/TagGoogle/TagGoogle.apk', 
    './GApps/dialergoogle/nodpi/priv-app/GoogleDialer/GoogleDialer.apk', 
    './GApps/contactsgoogle/nodpi/priv-app/GoogleContacts/GoogleContacts.apk' ]

def checkPrerequisites():
    tools = AAPT, ZIPALIGN
    for tool in tools:
        if os.system('which %s'%tool):
            print 'Please install %s in your PATH' %tool
            sys.exit(1)
    return True

def checkOpengappsBuildDir(path):
    return os.path.exists(path)

def prepareDirectories():
    VENDOR_DIR = os.path.join(os.path.dirname(__file__), '..', '..')
    def makedirs(path):
        if os.path.isdir(path):
            return
        os.makedirs(path)

    for dirname in (APPS_DIR,
                    os.path.join(DATA_DIR, ETC_DIR, PERMISSIONS_DIR),
                    os.path.join(DATA_DIR, ETC_DIR, PREFERRED_APPS_DIR),
                    os.path.join(DATA_DIR, ETC_DIR, SYSCONFIG_DIR),
                    FRAMEWORK_DIR, 
                    LIB_DIR):
        makedirs(os.path.join(VENDOR_DIR, dirname))
    return VENDOR_DIR

def copyOpenGappsFiles(build_path, opengapps_files, dst_dir, common_dir_depth):
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
        print 'Copying "%s" ...' % (inpfile)
        print '   ... to "%s"' % (outfile)
        shutil.copy(inpfile, outfile)

def apk_rename(filename):
    cmd = 'aapt d badging ' + filename
    print 'DEBUG : %s' % cmd
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

if __name__ == '__main__':
    checkPrerequisites()
    
    if len(sys.argv) != 2:
        print 'Usage: %s opengapps_build_path'%sys.argv[0]
        sys.exit(1)
    opengapps_path = os.path.join(sys.argv[1], ARCH, SDK, BUILD_VARIANT)
    
    if not checkOpengappsBuildDir(opengapps_path):
        print 'Error: %s is not a valid openGapps build directory.'%opengapps_path
        sys.exit(1)

    vendor_dir = prepareDirectories()
    
    # Copy xml files to vendor/google repo
    dst = os.path.join(vendor_dir, DATA_DIR)
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_DATA, dst, 3)
    # Copy facelock binary and so files to vendor/google repo
    dst = os.path.join(vendor_dir, LIB_DIR, 'facelock')
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_FACELOCK_6, dst, 6)
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_FACELOCK_5, dst, 5)
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_FACELOCK_2, dst, 2)
    # Copy jar files to vendor/google repo
    dst = vendor_dir
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_JAR, dst, 2)
    # Copy app libraries files to vendor/google repo
    dst = os.path.join(vendor_dir, APPS_DIR)
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_LIB, dst, 1)
    # Rename apps to package name and copy to google/vendor repo
    for apk in OPENGAPPS_APP:
        apk_filename = os.path.basename(apk)
        src = os.path.join(opengapps_path, apk)
        dst = os.path.join(vendor_dir, APPS_DIR, apk_filename)
        shutil.copy(src, dst)
        apk_rename(dst)
    # Rename priv-apps to package name and copy to google/vendor repo
    for apk in OPENGAPPS_PRIV_APP:
        apk_filename = os.path.basename(apk)
        src = os.path.join(opengapps_path, apk)
        dst = os.path.join(vendor_dir, APPS_DIR, apk_filename)
        shutil.copy(src, dst)
        apk_rename(dst)

