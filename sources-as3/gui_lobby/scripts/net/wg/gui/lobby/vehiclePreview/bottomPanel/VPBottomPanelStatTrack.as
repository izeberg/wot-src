package net.wg.gui.lobby.vehiclePreview.bottomPanel
{
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.lobby.vehiclePreview.data.VPStatTrackVO;
   import net.wg.infrastructure.base.meta.impl.VehiclePreviewBottomPanelStatTrackMeta;
   import net.wg.utils.IStageSizeDependComponent;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.motion.Tween;
   
   public class VPBottomPanelStatTrack extends VehiclePreviewBottomPanelStatTrackMeta implements IVPBottomPanel, IStageSizeDependComponent
   {
      
      private static const LABEL_OFFSET:int = 2;
      
      private static const INFO_ICON_OFFSET:int = 13;
      
      private static const SMALL_SCALE_VALUE:Number = 0.85;
      
      private static const HOVER_ANIMATION_DURATION:int = 500;
      
      private static const SMALL_HEIGHT_VALUE:int = 80;
      
      private static const NORMAL_HEIGHT_VALUE:int = 98;
       
      
      public var labelTF:TextField = null;
      
      public var infoIcon:Sprite = null;
      
      public var hitMc:Sprite = null;
      
      public var bgShine:Sprite = null;
      
      public var hover:Sprite = null;
      
      private var _isSmall:Boolean = false;
      
      private var _data:VPStatTrackVO = null;
      
      private var _hoverTween:Tween = null;
      
      public function VPBottomPanelStatTrack()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         hitArea = this.hitMc;
         addEventListener(MouseEvent.ROLL_OVER,this.onInfoRollOver);
         addEventListener(MouseEvent.ROLL_OUT,this.onInfoRollOut);
         this.bgShine.mouseChildren = this.bgShine.mouseEnabled = false;
         this.labelTF.autoSize = TextFieldAutoSize.LEFT;
         this.hover.alpha = Values.ZERO;
         App.stageSizeMgr.register(this);
      }
      
      override protected function draw() : void
      {
         if(isInvalid(InvalidationType.DATA) && this._data)
         {
            this.labelTF.text = this._data.label;
            this.labelTF.x = (-(this.labelTF.width + this.infoIcon.width + INFO_ICON_OFFSET) >> 1) + LABEL_OFFSET;
            this.infoIcon.x = this.labelTF.x + this.labelTF.width + INFO_ICON_OFFSET | 0;
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            scaleX = scaleY = !!this._isSmall ? Number(SMALL_SCALE_VALUE) : Number(1);
         }
      }
      
      override protected function onDispose() : void
      {
         App.stageSizeMgr.unregister(this);
         removeEventListener(MouseEvent.ROLL_OVER,this.onInfoRollOver);
         removeEventListener(MouseEvent.ROLL_OUT,this.onInfoRollOut);
         this.clearTweens();
         this.labelTF = null;
         this.infoIcon = null;
         this.hitMc = null;
         this.hover = null;
         this.bgShine = null;
         this._data = null;
         super.onDispose();
      }
      
      override protected function setData(param1:VPStatTrackVO) : void
      {
         this._data = param1;
         invalidateData();
      }
      
      public function getOffsetY() : int
      {
         return Values.ZERO;
      }
      
      public function getSmallScreenOffsetY() : int
      {
         return Values.ZERO;
      }
      
      public function getBtn() : SoundButtonEx
      {
         return null;
      }
      
      public function getTotalHeight() : Number
      {
         return Values.ZERO;
      }
      
      public function setStateSizeBoundaries(param1:int, param2:int) : void
      {
         var _loc3_:Boolean = param2 < StageSizeBoundaries.HEIGHT_900;
         if(_loc3_ == this._isSmall)
         {
            return;
         }
         this._isSmall = _loc3_;
         invalidateSize();
      }
      
      override public function get width() : Number
      {
         return Values.ZERO;
      }
      
      override public function get height() : Number
      {
         return !!this._isSmall ? Number(SMALL_HEIGHT_VALUE) : Number(NORMAL_HEIGHT_VALUE);
      }
      
      private function clearTweens() : void
      {
         if(this._hoverTween)
         {
            this._hoverTween.paused = true;
            this._hoverTween.dispose();
            this._hoverTween = null;
         }
      }
      
      private function onInfoRollOver(param1:MouseEvent) : void
      {
         this.clearTweens();
         this._hoverTween = new Tween(HOVER_ANIMATION_DURATION,this.hover,{"alpha":1});
         App.toolTipMgr.showWulfTooltip(TOOLTIPS_CONSTANTS.VEHICLE_STAT_TRACK);
      }
      
      private function onInfoRollOut(param1:MouseEvent) : void
      {
         this.clearTweens();
         this._hoverTween = new Tween(HOVER_ANIMATION_DURATION,this.hover,{"alpha":0});
         App.toolTipMgr.hide();
      }
   }
}
