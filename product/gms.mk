PRODUCT_PACKAGES := \
	Books \
	CloudPrint2 \
	Drive \
	PlusOne \
	FitnessPrebuilt \
	GoogleEars \
	Newsstand \
	PrebuiltKeep \
	PrebuiltBugle \
	EditorsDocs \
	EditorsSheets \
	EditorsSlides \
	PlayGames \
	PrebuiltNewsWeather \
	Translate \
	Videos \
	YouTube \
	talkback \

#PRODUCT_PACKAGES += \
	GoogleEarth \
	HangOutDialer \
	PdfViewer \

$(call inherit-product-if-exists, vendor/google/product/gms-core.mk)


