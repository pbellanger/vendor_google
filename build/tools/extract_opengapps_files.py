#!/usr/bin/env python
import os, sys
#import errno
#import glob
#import re
import shutil
#import struct
#import subprocess
#import zipfile

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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s opengapps_build_path'%sys.argv[0]
        sys.exit(1)
    opengapps_path = os.path.join(sys.argv[1], ARCH, SDK, BUILD_VARIANT)
    
    if not checkOpengappsBuildDir(opengapps_path):
        print 'Error: %s is not a valid openGapps build directory.'%opengapps_path
        sys.exit(1)

    vendor_dir = prepareDirectories()
    
    dst = os.path.join(vendor_dir, DATA_DIR)
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_DATA, dst, 3)
    dst = os.path.join(vendor_dir, LIB_DIR, 'facelock')
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_FACELOCK_6, dst, 6)
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_FACELOCK_5, dst, 5)
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_FACELOCK_2, dst, 2)
    dst = vendor_dir
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_JAR, dst, 2)
    dst = os.path.join(vendor_dir, APPS_DIR)
    copyOpenGappsFiles(opengapps_path, OPENGAPPS_LIB, dst, 1)

