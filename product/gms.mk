PRODUCT_PACKAGES := \
	Books \
	CloudPrint2 \
	Drive \
	PlusOne \
	FitnessPrebuilt \
	GoogleEars \
	Newsstand \
	PrebuiltKeep \
	EditorsDocs \
	EditorsSheets \
	EditorsSlides \
	PlayGames \
	PrebuiltNewsWeather \
	Translate \
	Videos \
	YouTube \
	talkback \
	GoogleEarth \

PRODUCT_PACKAGES += \
	PrebuiltBugle \
#	HangOutDialer \
#	PdfViewer \

$(call inherit-product-if-exists, vendor/google/product/gms-core.mk)


