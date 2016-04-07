GMS_FRWDIR := vendor/google/framework

GMS_JAR := \
	com.google.widevine.software.drm.jar \
	com.google.android.media.effects.jar \
	com.google.android.maps.jar \

ifeq ($(TARGET_PRODUCT),occam)
GMS_JAR += \
	com.google.android.camera2.jar \
        com.google.android.camera.experimental2015.jar \
	com.google.android.dialer.support.jar \

endif

define gms-copy-jar
$(eval PRODUCT_COPY_FILES += $(GMS_FRWDIR)/$(1):$(TARGET_COPY_OUT_SYSTEM)/framework/$(1):google)
endef

$(foreach f, $(GMS_JAR), $(call gms-copy-jar,$(f)))

GMS_FRWDIR :=

