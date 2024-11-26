package net.wg.gui.lobby.vehicleCustomization.controls
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.SoundTypes;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.CUSTOMIZATION_CONSTS;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.controls.ButtonIconTextTransparent;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.components.controls.TableRenderer;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.components.controls.price.CompoundPrice;
   import net.wg.gui.events.UILoaderEvent;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationPopoverItemRendererVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationIndicatorEvent;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class CustomizationPopoverItemRenderer extends TableRenderer
   {
      
      private static const NAME_X_NORMAL:int = 93;
      
      private static const NAME_X_TITLE:int = 13;
      
      private static const COUNTER_IN_STORAGE_OFFSET:int = 8;
      
      private static const COUNTER_IN_BASE_OFFSET:int = 3;
      
      private static const COUNTER_IN_PURCHASE_OFFSET:int = -3;
      
      private static const NON_HISTORIC_ICON_OFFSET:int = -10;
      
      private static const ICON_OFFSET:int = 51;
      
      private static const BACKGROUND_BIG:int = 70;
      
      private static const BACKGROUND_SMALL:int = 33;
      
      private static const ICON_BACKGROUND_OFFSET:int = 1;
      
      private static const RARITY_ICON_OFFSET:int = -3;
       
      
      public var nameTF:TextField = null;
      
      public var titleTF:TextField;
      
      public var titleBg:Sprite = null;
      
      public var rarityIcon:UILoaderAlt = null;
      
      public var rarityBg:UILoaderAlt = null;
      
      public var countTF:TextField = null;
      
      public var inStorageIcon:Image = null;
      
      public var iconBg:Sprite = null;
      
      public var itemIcon:UILoaderAlt = null;
      
      public var imageBg:MovieClip = null;
      
      public var price:CompoundPrice = null;
      
      public var customizationContentTypeIcon:Image = null;
      
      public var removeBtn:ButtonIconTextTransparent = null;
      
      private var _model:CustomizationPopoverItemRendererVO;
      
      private var _isAlreadyPurchased:Boolean = false;
      
      private var _tooltipManager:ITooltipMgr;
      
      public function CustomizationPopoverItemRenderer()
      {
         this._tooltipManager = App.toolTipMgr;
         super();
      }
      
      override public function setData(param1:Object) : void
      {
         super.setData(param1);
         this.itemIcon.unload();
         this.rarityBg.unload();
         this.rarityIcon.unload();
         this._tooltipManager.hide();
         this._model = Boolean(param1) ? CustomizationPopoverItemRendererVO(param1) : null;
         invalidateData();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.titleTF.mouseEnabled = false;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.removeBtn.addEventListener(ButtonEvent.CLICK,this.onRemoveBtnClickHandler);
         this.removeBtn.soundType = SoundTypes.CUSTOMIZATION_DEFAULT;
         this.removeBtn.mutedSoundTypes = [MouseEvent.MOUSE_DOWN];
         this.itemIcon.addEventListener(UILoaderEvent.COMPLETE,this.onItemIconLoaderCompleteHandler);
         addEventListener(MouseEvent.ROLL_OVER,this.onRollOverHandler);
         addEventListener(MouseEvent.ROLL_OUT,this.onRollOutHandler);
         this.countTF.autoSize = TextFieldAutoSize.RIGHT;
         this.inStorageIcon.source = RES_ICONS.MAPS_ICONS_CUSTOMIZATION_STORAGE_ICON;
      }
      
      override protected function draw() : void
      {
         var _loc1_:int = 0;
         super.draw();
         if(this._model)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               this.nameTF.htmlText = this._model.userName;
               App.utils.commons.truncateTextFieldText(this.nameTF,this._model.userName,true,true);
               this.titleTF.htmlText = this._model.titleLabel;
               this.titleBg.visible = this._model.isTitle;
               if(!this._model.isTitle)
               {
                  this._isAlreadyPurchased = this._model.isApplied;
                  this.updateVisibility(true);
                  this.itemIcon.visible = false;
                  this.imageBg.visible = false;
                  this.iconBg.visible = false;
                  this.countTF.htmlText = this._model.numItems;
                  this.itemIcon.source = this._model.icon;
                  if(this._model.customizationDisplayType == CUSTOMIZATION_CONSTS.NON_HISTORICAL_TYPE)
                  {
                     this.customizationContentTypeIcon.source = RES_ICONS.MAPS_ICONS_BUTTONS_NON_HISTORICAL;
                     this.customizationContentTypeIcon.visible = true;
                  }
                  else if(this._model.customizationDisplayType == CUSTOMIZATION_CONSTS.FANTASTICAL_TYPE)
                  {
                     this.customizationContentTypeIcon.source = RES_ICONS.MAPS_ICONS_BUTTONS_FANTASTICAL;
                     this.customizationContentTypeIcon.visible = true;
                  }
                  else
                  {
                     this.customizationContentTypeIcon.visible = false;
                  }
                  if(this._model.price)
                  {
                     this.price.setData(this._model.price);
                  }
                  this.rarityBg.visible = this.rarityIcon.visible = this._model.hasRarity;
                  this.rarityIcon.source = this._model.rarityIcon;
                  this.rarityBg.source = this._model.rarityBackground;
               }
               else
               {
                  this.nameTF.visible = true;
                  this.titleTF.visible = true;
                  this.price.visible = this.iconBg.visible = this.countTF.visible = this.itemIcon.visible = this.imageBg.visible = this.removeBtn.visible = this.inStorageIcon.visible = this.customizationContentTypeIcon.visible = this.rarityBg.visible = this.rarityIcon.visible = false;
               }
               this.layoutName(this._model.isTitle);
               invalidateSize();
            }
            if(isInvalid(InvalidationType.SIZE))
            {
               if(!this._model.isTitle)
               {
                  this.layoutItemIcon();
                  if(!this._isAlreadyPurchased)
                  {
                     if(this.inStorageIcon.visible)
                     {
                        this.countTF.x = this.inStorageIcon.x - this.countTF.width + COUNTER_IN_STORAGE_OFFSET ^ 0;
                     }
                     else
                     {
                        this.countTF.x = this.price.x + this.price.hit.x - this.countTF.width + COUNTER_IN_BASE_OFFSET ^ 0;
                     }
                  }
                  else
                  {
                     this.countTF.x = this.removeBtn.x - this.countTF.width + COUNTER_IN_PURCHASE_OFFSET ^ 0;
                  }
                  this.customizationContentTypeIcon.x = this.itemIcon.x + this.itemIcon.width + NON_HISTORIC_ICON_OFFSET ^ 0;
                  this.rarityBg.x = this.itemIcon.x;
                  this.rarityBg.y = this.itemIcon.y;
                  this.rarityBg.width = this.itemIcon.width;
                  this.rarityBg.height = this.itemIcon.height;
                  this.rarityIcon.x = this.itemIcon.x + RARITY_ICON_OFFSET;
                  this.rarityIcon.y = this.itemIcon.y + RARITY_ICON_OFFSET;
                  _loc1_ = !!this._model.isWide ? int(BACKGROUND_BIG) : int(BACKGROUND_SMALL);
                  this.imageBg.width = this.iconBg.width = _loc1_;
                  this.imageBg.height = this.iconBg.height = this.itemIcon.height + (ICON_BACKGROUND_OFFSET << 1) ^ 0;
                  this.imageBg.x = this.iconBg.x = this.itemIcon.x - (this.iconBg.width - this.itemIcon.width >> 1) ^ 0;
                  this.imageBg.y = this.iconBg.y = this.itemIcon.y - ICON_BACKGROUND_OFFSET;
               }
            }
         }
         else
         {
            this.updateVisibility(false);
         }
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(MouseEvent.ROLL_OVER,this.onRollOverHandler);
         removeEventListener(MouseEvent.ROLL_OUT,this.onRollOutHandler);
         this.removeBtn.removeEventListener(ButtonEvent.CLICK,this.onRemoveBtnClickHandler);
         this.removeBtn.dispose();
         this.removeBtn = null;
         this.itemIcon.removeEventListener(UILoaderEvent.COMPLETE,this.onItemIconLoaderCompleteHandler);
         this.itemIcon.dispose();
         this.itemIcon = null;
         this.price.dispose();
         this.price = null;
         this.rarityIcon.dispose();
         this.rarityIcon = null;
         this.rarityBg.dispose();
         this.rarityBg = null;
         this.inStorageIcon.dispose();
         this.inStorageIcon = null;
         this.customizationContentTypeIcon.dispose();
         this.customizationContentTypeIcon = null;
         this.iconBg = null;
         this.nameTF = null;
         this.titleTF = null;
         this.countTF = null;
         this.titleBg = null;
         this._model = null;
         this._tooltipManager = null;
         this.imageBg = null;
         super.onDispose();
      }
      
      protected function layoutItemIcon() : void
      {
         this.itemIcon.x = ICON_OFFSET - (this.itemIcon.width >> 1) ^ 0;
      }
      
      protected function layoutName(param1:Boolean) : void
      {
         this.nameTF.x = !!param1 ? Number(NAME_X_TITLE) : Number(NAME_X_NORMAL);
      }
      
      protected function updateVisibility(param1:Boolean) : void
      {
         this.enabled = param1;
         this.nameTF.visible = param1;
         this.titleTF.visible = param1;
         this.iconBg.visible = param1;
         this.countTF.visible = param1;
         this.itemIcon.visible = param1;
         this.rarityBg.visible = param1;
         this.rarityIcon.visible = param1;
         this.removeBtn.visible = param1;
         var _loc2_:Boolean = param1 && this._model;
         this.customizationContentTypeIcon.visible = _loc2_ && this._model.customizationDisplayType != CUSTOMIZATION_CONSTS.HISTORICAL_TYPE;
         this.imageBg.visible = _loc2_ && this._model.isDim;
         this.price.visible = _loc2_ && this._model.price && !this._model.isApplied;
         this.inStorageIcon.visible = param1 && !this.price.visible && !this._model.isApplied;
      }
      
      protected function removeItem() : void
      {
         dispatchEvent(new CustomizationIndicatorEvent(CustomizationIndicatorEvent.REMOVAL,this._model.id,this._model.itemsList,this._model.seasonType));
      }
      
      override public function set enabled(param1:Boolean) : void
      {
         super.enabled = param1;
         mouseChildren = param1;
      }
      
      private function onRollOverHandler(param1:MouseEvent) : void
      {
         if(this._model && this._model.id != Values.DEFAULT_INT)
         {
            this._tooltipManager.showSpecial(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM,null,this._model.id,-1,true,this._model.progressionLevel);
         }
      }
      
      private function onItemIconLoaderCompleteHandler(param1:UILoaderEvent) : void
      {
         invalidateSize();
         this.itemIcon.visible = this.iconBg.visible = this.rarityIcon.visible = this.rarityBg.visible = true;
         this.imageBg.visible = this._model && this._model.isDim;
      }
      
      private function onRollOutHandler(param1:MouseEvent) : void
      {
         this._tooltipManager.hide();
      }
      
      private function onRemoveBtnClickHandler(param1:ButtonEvent) : void
      {
         this._tooltipManager.hide();
         this.removeItem();
         this.setData(null);
      }
   }
}
