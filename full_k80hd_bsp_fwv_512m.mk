# Inherit from those products. Most specific first.
#$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base.mk)

# Set target and base project for flavor build
MTK_TARGET_PROJECT := $(subst full_,,$(TARGET_PRODUCT))
MTK_BASE_PROJECT := $(MTK_TARGET_PROJECT)
MTK_PROJECT_FOLDER := $(LOCAL_PATH)
MTK_TARGET_PROJECT_FOLDER := $(LOCAL_PATH)

# This is where we'd set a backup provider if we had one
#$(call inherit-product, device/sample/products/backup_overlay.mk)
$(call inherit-product, $(LOCAL_PATH)/device.mk)

include $(LOCAL_PATH)/ProjectConfig.mk
# set locales & aapt config.
PRODUCT_LOCALES := en_US bn_IN zh_CN ur_PK vi_VN
# Set those variables here to overwrite the inherited values.
PRODUCT_MANUFACTURER := alps
PRODUCT_NAME := full_k80hd_bsp_fwv_512m
PRODUCT_DEVICE := k80hd_bsp_fwv_512m
PRODUCT_MODEL := V48
PRODUCT_POLICY := android.policy_phone
PRODUCT_BRAND := Symphony

ifeq ($(TARGET_BUILD_VARIANT), eng)
KERNEL_DEFCONFIG ?= k80hd_bsp_fwv_512m_debug_defconfig
else
KERNEL_DEFCONFIG ?= k80hd_bsp_fwv_512m_defconfig
endif
PRELOADER_TARGET_PRODUCT ?= k80hd_bsp_fwv_512m
LK_PROJECT ?= k80hd_bsp_fwv_512m
TRUSTY_PROJECT ?= k80hd_bsp_fwv_512m

#A-GO
PRODUCT_MINIMIZE_JAVA_DEBUG_INFO := true
$(call inherit-product-if-exists, frameworks/base/data/sounds/AudioPackageGo.mk)
