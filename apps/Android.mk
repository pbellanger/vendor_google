LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
# Chrome : 49.0.2623.105
LOCAL_MODULE := Chrome
LOCAL_SRC_FILES := com.android.chrome.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Browser
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# FaceLock : 6.0.1
LOCAL_MODULE := FaceLock
LOCAL_SRC_FILES := com.android.facelock.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleCamera : 3.1.025 (2617469-30)
LOCAL_MODULE := GoogleCamera
LOCAL_SRC_FILES := com.google.android.GoogleCamera.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Camera2
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Books : 3.7.75
LOCAL_MODULE := Books
LOCAL_SRC_FILES := com.google.android.apps.books.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# CloudPrint2 : 1.33b
LOCAL_MODULE := CloudPrint2
LOCAL_SRC_FILES := com.google.android.apps.cloudprint.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Drive : 2.3.631.15.30
LOCAL_MODULE := Drive
LOCAL_SRC_FILES := com.google.android.apps.docs.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# EditorsDocs : 1.6.112.12.30
LOCAL_MODULE := EditorsDocs
LOCAL_SRC_FILES := com.google.android.apps.docs.editors.docs.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# EditorsSheets : 1.6.112.06.30
LOCAL_MODULE := EditorsSheets
LOCAL_SRC_FILES := com.google.android.apps.docs.editors.sheets.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# EditorsSlides : 1.6.112.10.30
LOCAL_MODULE := EditorsSlides
LOCAL_SRC_FILES := com.google.android.apps.docs.editors.slides.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# FitnessPrebuilt : 1.56.14-000
LOCAL_MODULE := FitnessPrebuilt
LOCAL_SRC_FILES := com.google.android.apps.fitness.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PrebuiltNewsWeather : 2.5.2 (105241914)
LOCAL_MODULE := PrebuiltNewsWeather
LOCAL_SRC_FILES := com.google.android.apps.genie.geniewidget.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Newsstand : 3.5.1
LOCAL_MODULE := Newsstand
LOCAL_SRC_FILES := com.google.android.apps.magazines.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Maps : 9.22.1
LOCAL_MODULE := Maps
LOCAL_SRC_FILES := com.google.android.apps.maps.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Photos : 1.16.0.117494210
LOCAL_MODULE := Photos
LOCAL_SRC_FILES := com.google.android.apps.photos.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := VisualizationWallpapers Gallery2 PhotoTable LiveWallpapers Galaxy4 HoloSpiralWallpaper NoiseField PhaseBeam
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PlusOne : 7.5.0.117765045
LOCAL_MODULE := PlusOne
LOCAL_SRC_FILES := com.google.android.apps.plus.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Translate : 4.4.0.RC01.104701208
LOCAL_MODULE := Translate
LOCAL_SRC_FILES := com.google.android.apps.translate.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# CalculatorGoogle : 5.2 (2419427)
LOCAL_MODULE := CalculatorGoogle
LOCAL_SRC_FILES := com.google.android.calculator.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Calculator ExactCalculator
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# CalendarGooglePrebuilt : 5.3.8-117343094-release
LOCAL_MODULE := CalendarGooglePrebuilt
LOCAL_SRC_FILES := com.google.android.calendar.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Calendar
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PrebuiltDeskClockGoogle : 4.3 (2552012)
LOCAL_MODULE := PrebuiltDeskClockGoogle
LOCAL_SRC_FILES := com.google.android.deskclock.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := DeskClock
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleEars : 1.2.0
LOCAL_MODULE := GoogleEars
LOCAL_SRC_FILES := com.google.android.ears.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PrebuiltGmail : 6.0.115979076.release
LOCAL_MODULE := PrebuiltGmail
LOCAL_SRC_FILES := com.google.android.gm.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Email
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PrebuiltExchange3Google : 5.0.106634657
LOCAL_MODULE := PrebuiltExchange3Google
LOCAL_SRC_FILES := com.google.android.gm.exchange.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Exchange2
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# LatinImeGoogle : 4.1.23163.2622203
LOCAL_MODULE := LatinImeGoogle
LOCAL_SRC_FILES := com.google.android.inputmethod.latin.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := LatinIME OpenWnn
LOCAL_REQUIRED_MODULES := libjni_keyboarddecoder libjni_latinimegoogle
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PrebuiltKeep : 3.3.102.0
LOCAL_MODULE := PrebuiltKeep
LOCAL_SRC_FILES := com.google.android.keep.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleHome : 1.3.large
LOCAL_MODULE := GoogleHome
LOCAL_SRC_FILES := com.google.android.launcher.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Launcher2
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# talkback : 4.4.1
LOCAL_MODULE := talkback
LOCAL_SRC_FILES := com.google.android.marvin.talkback.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Music2 : 6.5.2513X.2681020
LOCAL_MODULE := Music2
LOCAL_SRC_FILES := com.google.android.music.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Music
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PlayGames : 3.6.27 (2647216-030)
LOCAL_MODULE := PlayGames
LOCAL_SRC_FILES := com.google.android.play.games.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleContactsSyncAdapter : 6.0.1
LOCAL_MODULE := GoogleContactsSyncAdapter
LOCAL_SRC_FILES := com.google.android.syncadapters.contacts.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleTTS : 3.8.16
LOCAL_MODULE := GoogleTTS
LOCAL_SRC_FILES := com.google.android.tts.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := PicoTts
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Videos : 3.12.10
LOCAL_MODULE := Videos
LOCAL_SRC_FILES := com.google.android.videos.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Wallet : 1.2.111627672
LOCAL_MODULE := Wallet
LOCAL_SRC_FILES := com.google.android.apps.walletnfcrel.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# WebViewGoogle : 48.0.2564.106
LOCAL_MODULE := WebViewGoogle
LOCAL_SRC_FILES := com.google.android.webview.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := webview
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# YouTube : 11.10.57
LOCAL_MODULE := YouTube
LOCAL_SRC_FILES := com.google.android.youtube.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleEarth : 8.0.2.2334
LOCAL_MODULE := GoogleEarth
LOCAL_SRC_FILES := com.google.earth.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# EditorsDocsStub : 1.6.112.12.30
LOCAL_MODULE := EditorsDocsStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.docs.editors.docs.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := EditorsDocs
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# EditorsSheetsStub : 1.6.112.06.30
LOCAL_MODULE := EditorsSheetsStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.docs.editors.sheets.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := EditorsSheets
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# EditorsSlidesStub : 1.6.112.10.30
LOCAL_MODULE := EditorsSlidesStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.docs.editors.slides.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := EditorsSlides
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# NewsstandStub : 3.5.1
LOCAL_MODULE := NewsstandStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.magazines.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Newsstand
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PrebuiltKeepStub : 3.3.102.0
LOCAL_MODULE := PrebuiltKeepStub
LOCAL_SRC_FILES := stubs/com.google.android.keep.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := PrebuiltKeep
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# BooksStub : 3.7.75
LOCAL_MODULE := BooksStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.books.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Books
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# CloudPrint2Stub : 1.33b
LOCAL_MODULE := CloudPrint2Stub
LOCAL_SRC_FILES := stubs/com.google.android.apps.cloudprint.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := CloudPrint2
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# DriveStub : 2.3.631.15.30
LOCAL_MODULE := DriveStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.docs.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Drive
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# FitnessPrebuiltStub : 1.56.14-000
LOCAL_MODULE := FitnessPrebuiltStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.fitness.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := FitnessPrebuilt
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# MapsStub : 9.22.1
LOCAL_MODULE := MapsStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.maps.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Maps
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PlusOneStub : 7.5.0.117765045
LOCAL_MODULE := PlusOneStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.plus.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := PlusOne
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# TranslateStub : 4.4.0.RC01.104701208
LOCAL_MODULE := TranslateStub
LOCAL_SRC_FILES := stubs/com.google.android.apps.translate.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Translate
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# VideosStub : 3.12.10
LOCAL_MODULE := VideosStub
LOCAL_SRC_FILES := stubs/com.google.android.videos.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Videos
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# YouTubeStub : 11.10.57
LOCAL_MODULE := YouTubeStub
LOCAL_SRC_FILES := stubs/com.google.android.youtube.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := YouTube
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Phonesky : 6.3.16.B-all [0] 2697688
LOCAL_MODULE := Phonesky
LOCAL_SRC_FILES := com.android.vending.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# AndroidForWork : 6.0-2280749
LOCAL_MODULE := AndroidForWork
LOCAL_SRC_FILES := com.google.android.androidforwork.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GCS : C.1.6.7 (2466695)
LOCAL_MODULE := GCS
LOCAL_SRC_FILES := com.google.android.apps.gcs.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# ConfigUpdater : 6.0.1
LOCAL_MODULE := ConfigUpdater
LOCAL_SRC_FILES := com.google.android.configupdater.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleContacts : 1.4.2
LOCAL_MODULE := GoogleContacts
LOCAL_SRC_FILES := com.google.android.contacts.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Contacts
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleDialer : 2.3.17
LOCAL_MODULE := GoogleDialer
LOCAL_SRC_FILES := com.google.android.dialer.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Dialer
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleFeedback : 6.0.1
LOCAL_MODULE := GoogleFeedback
LOCAL_SRC_FILES := com.google.android.feedback.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# Velvet : 5.10.32.19.arm
LOCAL_MODULE := Velvet
LOCAL_SRC_FILES := com.google.android.googlequicksearchbox.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := QuickSearchBox
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# PrebuiltGmsCore : 8.7.03 (2645110-430)
LOCAL_MODULE := PrebuiltGmsCore
LOCAL_SRC_FILES := com.google.android.gms.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := WAPPushManager
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleServicesFramework : 6.0.1
LOCAL_MODULE := GoogleServicesFramework
LOCAL_SRC_FILES := com.google.android.gsf.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleLoginService : 6.0.1
LOCAL_MODULE := GoogleLoginService
LOCAL_SRC_FILES := com.google.android.gsf.login.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleOneTimeInitializer : 6.0.1
LOCAL_MODULE := GoogleOneTimeInitializer
LOCAL_SRC_FILES := com.google.android.onetimeinitializer.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := OneTimeInitializer
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GooglePackageInstaller : 6.0.1
LOCAL_MODULE := GooglePackageInstaller
LOCAL_SRC_FILES := com.google.android.packageinstaller.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := PackageInstaller
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GooglePartnerSetup : 6.0.1
LOCAL_MODULE := GooglePartnerSetup
LOCAL_SRC_FILES := com.google.android.partnersetup.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# SetupWizard : 2.0
LOCAL_MODULE := SetupWizard
LOCAL_SRC_FILES := com.google.android.setupwizard.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Provision
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# TagGoogle : 1.1
LOCAL_MODULE := TagGoogle
LOCAL_SRC_FILES := com.google.android.tag.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := Tag
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
# GoogleBackupTransport : 6.0.1
LOCAL_MODULE := GoogleBackupTransport
LOCAL_SRC_FILES := com.google.android.backuptransport.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_PRIVILEGED_MODULE := true
LOCAL_MODULE_OWNER := google
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

