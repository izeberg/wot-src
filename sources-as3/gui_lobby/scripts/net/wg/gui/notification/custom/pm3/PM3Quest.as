package net.wg.gui.notification.custom.pm3
{
   import flash.display.DisplayObject;
   import flash.display.Sprite;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormatAlign;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.notification.ServiceMessageContent;
   import net.wg.gui.notification.custom.vo.PM3QuestVO;
   import net.wg.infrastructure.interfaces.IDisposableSprite;
   import net.wg.utils.IClassFactory;
   
   public class PM3Quest extends ServiceMessageContent
   {
      
      private static const MESSAGE_WIDTH:uint = 289;
      
      private static const FOOTER_TOP_PADDING:uint = 10;
      
      private static const BOTTOM_MARGIN:uint = 10;
      
      private static const BOTTOM_MARGIN_COMPLETED:uint = 30;
      
      private static const OVERLAY_PADDING_TOP:uint = 19;
      
      private static const OVERLAY_COMPLETED_PADDING_TOP:uint = 24;
      
      private static const OVERLAY_PADDING_BOTTOM:uint = 16;
      
      private static const MISSION_LEFT_MARGIN:uint = 4;
      
      private static const WIDTH:int = 288;
      
      private static const BUTTONS_GROUP_OFFSET_Y:int = 30;
      
      private static const CUT_SYMBOLS_STR:String = "..";
      
      private static const HYPHEN:String = "-";
      
      private static const TEXT_FIELD_BOUNDS_WIDTH:uint = 10;
       
      
      public var missionName:TextField = null;
      
      public var category:UILoaderAlt = null;
      
      public var bgImg:Sprite = null;
      
      public var bgMask:Sprite = null;
      
      public var centerOverlay:Sprite = null;
      
      private var _description:IDisposableSprite = null;
      
      private var _footer:IDisposableSprite = null;
      
      private var _classFactory:IClassFactory = null;
      
      public function PM3Quest()
      {
         buttonsAlign = TextFormatAlign.CENTER;
         this._classFactory = App.utils.classFactory;
         super();
      }
      
      override protected function onDispose() : void
      {
         this._classFactory = null;
         this.clearLinkages();
         this.category.dispose();
         this.category = null;
         this.bgImg = null;
         this.bgMask = null;
         this.centerOverlay = null;
         this.missionName = null;
         super.onDispose();
      }
      
      private function clearLinkages() : void
      {
         if(this._description != null)
         {
            removeChild(DisplayObject(this._description));
            this._description.dispose();
            this._description = null;
         }
         if(this._footer != null)
         {
            removeChild(DisplayObject(this._footer));
            this._footer.dispose();
            this._footer = null;
         }
      }
      
      override protected function processCustomData(param1:Object) : void
      {
         var _loc5_:PM3DescriptionCompleted = null;
         var _loc6_:PM3FooterCompleted = null;
         var _loc7_:PM3DescriptionUncompleted = null;
         var _loc8_:PM3FooterUncompleted = null;
         var _loc2_:PM3QuestVO = new PM3QuestVO(param1);
         this.category.source = RES_ICONS.getPM3Category36x36(_loc2_.category);
         this.formatMissionNameWithEllipsis(this.missionName,_loc2_.mission,HYPHEN + _loc2_.missionNumber);
         var _loc3_:int = this.category.originalWidth + MISSION_LEFT_MARGIN + Math.min(this.missionName.textWidth,this.missionName.width);
         this.category.x = WIDTH - _loc3_ >> 1;
         this.missionName.x = this.category.x + this.category.originalWidth + MISSION_LEFT_MARGIN;
         this.clearLinkages();
         if(_loc2_.isCompleted)
         {
            _loc5_ = this._classFactory.getComponent(Linkages.PM3_SYS_MES_DESCR_COMPLETED_UI,PM3DescriptionCompleted);
            _loc6_ = this._classFactory.getComponent(Linkages.PM3_SYS_MES_FOOTER_COMPLETED_UI,PM3FooterCompleted);
            _loc6_.setData(_loc2_.awards);
            this._description = _loc5_;
            this._footer = _loc6_;
         }
         else
         {
            _loc7_ = this._classFactory.getComponent(Linkages.PM3_SYS_MES_DESCR_UPCOMPLETED_UI,PM3DescriptionUncompleted);
            _loc8_ = this._classFactory.getComponent(Linkages.PM3_SYS_MES_FOOTER_UPCOMPLETED_UI,PM3FooterUncompleted);
            _loc7_.setData(_loc2_.status,_loc2_.vehicles,_loc2_.allVehs);
            this._description = _loc7_;
            this._footer = _loc8_;
         }
         addChild(DisplayObject(this._description));
         addChild(DisplayObject(this._footer));
         var _loc4_:int = !!_loc2_.isCompleted ? int(OVERLAY_COMPLETED_PADDING_TOP) : int(OVERLAY_PADDING_TOP);
         this.centerOverlay.y = this.missionName.y + this.missionName.textHeight + _loc4_ >> 0;
         this.centerOverlay.height = this._description.height + OVERLAY_PADDING_BOTTOM >> 0;
         this._description.y = this.centerOverlay.y;
         this._footer.y = this.centerOverlay.y + this.centerOverlay.height + FOOTER_TOP_PADDING >> 0;
         super.processCustomData(param1);
      }
      
      override protected function updateData() : void
      {
         if(!data)
         {
            return;
         }
         super.updateData();
      }
      
      override protected function updateLayout() : void
      {
         super.updateLayout();
         var _loc1_:Rectangle = this.updateBackgroundSize();
         this.bgMask.height = _loc1_.height;
         this.bgImg.y = this.bgMask.height - this.bgImg.height >> 1;
      }
      
      override protected function updateBackgroundSize() : Rectangle
      {
         if(buttonsGroup != null)
         {
            return new Rectangle(0,0,WIDTH,buttonsGroup.y + buttonsGroup.height + BOTTOM_MARGIN_COMPLETED);
         }
         return new Rectangle(0,0,WIDTH,this._footer.y + this._footer.height + BOTTOM_MARGIN);
      }
      
      override protected function get buttonsAnchorVertical() : DisplayObject
      {
         return Boolean(this._footer) ? DisplayObject(this._footer) : textField;
      }
      
      override protected function get buttonsGroupPaddingTop() : int
      {
         return BUTTONS_GROUP_OFFSET_Y;
      }
      
      override public function get width() : Number
      {
         return MESSAGE_WIDTH;
      }
      
      private function formatMissionNameWithEllipsis(param1:TextField, param2:String, param3:String) : void
      {
         var _loc7_:String = null;
         this.missionName.text = param2 + param3;
         param1.autoSize = TextFieldAutoSize.NONE;
         param1.wordWrap = false;
         var _loc4_:Number = param1.width;
         var _loc5_:int = param2.length;
         var _loc6_:String = param2 + param3;
         if(param1.textWidth <= _loc4_)
         {
            param1.text = _loc6_;
            return;
         }
         do
         {
            _loc7_ = param2.substr(0,_loc5_) + CUT_SYMBOLS_STR;
            _loc6_ = _loc7_ + param3;
            param1.text = _loc6_;
            param1.getLineMetrics(0);
            _loc5_--;
         }
         while(param1.textWidth + TEXT_FIELD_BOUNDS_WIDTH > _loc4_ && _loc5_ >= 0);
         
         param1.text = _loc6_;
      }
   }
}
