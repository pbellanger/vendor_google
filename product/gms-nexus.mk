PRODUCT_PACKAGES := \
	Chrome \
	Photos \
	CalculatorGoogle \
	CalendarGooglePrebuilt \
	PrebuiltDeskClockGoogle \
	PrebuiltGmail \
	PrebuiltExchange3Google \
	LatinImeGoogle \
	GoogleHome \
	Music2 \
#	Hangouts \
	GoogleTTS \
	GoogleContacts \
	GoogleFeedback \
	TagGoogle \

ifeq ($(TARGET_PRODUCT),occam)
PRODUCT_PACKAGES += \
	GoogleCamera \
	GoogleDialer \

endif

PRODUCT_PROPERTY_OVERRIDES += \
	ro.error.receiver.system.apps=com.google.android.gms \

$(call inherit-product-if-exists, vendor/google/product/gms-jar.mk)
$(call inherit-product-if-exists, vendor/google/product/gms-lib.mk)
$(call inherit-product-if-exists, vendor/google/product/data.mk)

