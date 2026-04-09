package net.wg.gui.lobby.storage.categories.cards
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.components.controls.price.CompoundPrice;
   import net.wg.gui.components.paginator.vo.ToolTipVO;
   import net.wg.gui.lobby.storage.categories.cards.configs.CardConfigs;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.motion.Tween;
   
   public class RestoreDeviceCard extends RestoreBaseCard
   {
      
      private static const INFO_ICON_RIGHT_OFFSET:int = -12;
      
      private static const INFO_ICON_TOP_OFFSET:int = 10;
       
      
      public var availableToRestoreTF:TextField = null;
      
      public var info:MovieClip = null;
      
      public var compoundPrice:CompoundPrice = null;
      
      private var _infoImage:Image = null;
      
      public function RestoreDeviceCard()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         this._infoImage = this.info.image;
         super.initialize();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.info.buttonMode = true;
         this.info.addEventListener(MouseEvent.ROLL_OVER,this.onInfoRollOverHandler);
         this.info.addEventListener(MouseEvent.ROLL_OUT,this.onInfoRollOutHandler);
         this._infoImage.mouseChildren = this._infoImage.mouseEnabled = false;
         this._infoImage.addEventListener(Event.CHANGE,this.onInfoImageCompleteHandler);
         this._infoImage.source = RES_ICONS.MAPS_ICONS_LIBRARY_INFO_GRAY;
         this.compoundPrice.useSymmetricLayout = true;
         this.compoundPrice.itemsDirection = CompoundPrice.DIRECTION_RIGHT;
      }
      
      override protected function onDispose() : void
      {
         this._infoImage.removeEventListener(Event.CHANGE,this.onInfoImageCompleteHandler);
         this._infoImage.dispose();
         this._infoImage = null;
         this.info.removeEventListener(MouseEvent.ROLL_OVER,this.onInfoRollOverHandler);
         this.info.removeEventListener(MouseEvent.ROLL_OUT,this.onInfoRollOutHandler);
         this.info = null;
         this.compoundPrice.dispose();
         this.compoundPrice = null;
         this.availableToRestoreTF = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:RestoreDeviceCardVO = null;
         var _loc2_:Rectangle = null;
         super.draw();
         if(_data)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               _loc1_ = RestoreDeviceCardVO(_data);
               if(_loc1_.availableToRestore)
               {
                  this.availableToRestoreTF.htmlText = _loc1_.availableToRestore;
               }
               this.availableToRestoreTF.visible = StringUtils.isNotEmpty(_loc1_.availableToRestore);
               if(_resetViewOnDataChange)
               {
                  this.availableToRestoreTF.alpha = 1;
               }
            }
            if(isInvalid(InvalidationType.SIZE))
            {
               _loc2_ = _sizeVO.innerPadding;
               this.availableToRestoreTF.x = _loc2_.right - this.availableToRestoreTF.width >> 0;
               this.availableToRestoreTF.y = _loc2_.bottom - this.availableToRestoreTF.height >> 0;
               this.info.x = _loc2_.right + INFO_ICON_RIGHT_OFFSET;
               this.info.y = _loc2_.top + INFO_ICON_TOP_OFFSET;
               this.compoundPrice.x = _loc2_.left;
               this.compoundPrice.y = _loc2_.bottom - this.compoundPrice.hit.height >> 0;
               if(!_isOver)
               {
                  _container.y = this.getContainerYRolloutPosition();
               }
            }
         }
      }
      
      override public function setStateSizeBoundaries(param1:int, param2:int) : void
      {
         super.setStateSizeBoundaries(param1,param2);
         _imageSizeVO = CardConfigs.getInstance().restoreDeviceCardImage.getConfig(_stageWidthBoundary);
      }
      
      override protected function getRollOverTweens() : Vector.<Tween>
      {
         var _loc1_:Vector.<Tween> = super.getRollOverTweens();
         _loc1_.push(new Tween(FIRST_ANIMATION_DURATION,this.availableToRestoreTF,{"alpha":0},{
            "fastTransform":false,
            "delay":ROLL_OVER_ANIMATION_DELAY
         }));
         _loc1_.push(new Tween(FIRST_ANIMATION_DURATION,timerTF,{"alpha":0},{
            "fastTransform":false,
            "delay":ROLL_OVER_ANIMATION_DELAY
         }));
         _loc1_.push(new Tween(FIRST_ANIMATION_DURATION,timerImage,{"alpha":0},{
            "fastTransform":false,
            "delay":ROLL_OVER_ANIMATION_DELAY
         }));
         return _loc1_;
      }
      
      override protected function getRollOutTweens() : Vector.<Tween>
      {
         var _loc1_:Vector.<Tween> = super.getRollOutTweens();
         _loc1_.push(new Tween(FIRST_ANIMATION_DURATION,this.availableToRestoreTF,{"alpha":1},{"fastTransform":false}));
         _loc1_.push(new Tween(FIRST_ANIMATION_DURATION,timerTF,{"alpha":1},{"fastTransform":false}));
         _loc1_.push(new Tween(FIRST_ANIMATION_DURATION,timerImage,{"alpha":1},{"fastTransform":false}));
         return _loc1_;
      }
      
      override protected function drawPrice() : void
      {
         var _loc1_:RestoreDeviceCardVO = RestoreDeviceCardVO(_data);
         this.compoundPrice.setData(_loc1_.price);
         this.compoundPrice.updateEnoughStatuses(_loc1_.isEnoughStatuses);
         this.compoundPrice.validateNow();
         this.compoundPrice.actionTooltip = _loc1_.price.action;
      }
      
      override protected function getContainerYRolloutPosition() : int
      {
         return this.compoundPrice.y - titleTF.height >> 0;
      }
      
      private function onInfoRollOverHandler(param1:MouseEvent) : void
      {
         var _loc2_:ToolTipVO = RestoreDeviceCardVO(_data).infoTooltipData;
         if(_loc2_)
         {
            App.toolTipMgr.showSpecial.apply(this,[_loc2_.specialAlias,null].concat(_loc2_.specialArgs));
         }
      }
      
      private function onInfoRollOutHandler(param1:MouseEvent) : void
      {
         App.toolTipMgr.hide();
      }
      
      private function onInfoImageCompleteHandler(param1:Event) : void
      {
         this._infoImage.removeEventListener(Event.CHANGE,this.onInfoImageCompleteHandler);
         this._infoImage.x = -this._infoImage.width >> 1;
         this._infoImage.y = -this._infoImage.height >> 1;
      }
   }
}
