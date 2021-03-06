GMS_DATA_DIR := vendor/google/data

GMS_DATA_FILES := \
        etc/permissions/com.google.android.maps.xml \
        etc/permissions/com.google.android.media.effects.xml \
        etc/permissions/com.google.widevine.software.drm.xml \
        etc/preferred-apps/google.xml \
        etc/sysconfig/google.xml \
        etc/sysconfig/google_build.xml \
        etc/sysconfig/whitelist_com.android.omadm.service.xml \

ifeq ($(TARGET_PRODUCT),occam)
GMS_DATA_FILES += \
#        etc/permissions/com.google.android.camera2.xml \
        etc/permissions/com.google.android.camera.experimental2015.xml \
        etc/permissions/com.google.android.dialer.support.xml \

endif

define copy-gms-files
$(eval PRODUCT_COPY_FILES += $(GMS_DATA_DIR)/$(1):$(TARGET_COPY_OUT_SYSTEM)/$(1):google)
endef

$(foreach f, $(GMS_DATA_FILES) ,$(call copy-gms-files,$(f)))
