PRODUCT_PACKAGES := \
	Books \
	CloudPrint2 \
#	Drive \
	PlusOne \
	FitnessPrebuilt \
	GoogleEars \
	Newsstand \
	PrebuiltKeep \
#	EditorsDocs \
#	EditorsSheets \
#	EditorsSlides \
	PlayGames \
	PrebuiltNewsWeather \
	Translate \
	Videos \
	YouTube \
	talkback \
	PrebuiltBugle \
#	HangOutDialer \
#	PdfViewer \

ifeq ($(TARGET_PRODUCT),occam)
PRODUCT_PACKAGES += \
	GoogleEarth \

endif

$(call inherit-product-if-exists, vendor/google/product/gms-core.mk)


