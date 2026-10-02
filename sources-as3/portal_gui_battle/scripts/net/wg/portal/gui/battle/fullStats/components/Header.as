package net.wg.portal.gui.battle.fullStats.components
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.components.controls.Image;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.portal.data.VO.fullStats.PortalEventHeaderVO;
   import net.wg.utils.StageBreakPointList;
   
   public class Header extends SimpleDisposable
   {
      
      private static const ICON_MARGIN_X:Number = 8;
      
      private static const HEADER_BG_HEIGHT:uint = 135;
      
      private static const HEADER_BG_HEIGHT_EXTRA_LARGE:uint = 200;
       
      
      public var battleIcon:Image = null;
      
      public var titleTF:TextField = null;
      
      public var subTitleTF:TextField = null;
      
      public var descriptionTF:TextField = null;
      
      public var headerBG:Sprite = null;
      
      public function Header()
      {
         super();
         this.initialiaze();
      }
      
      override protected function onDispose() : void
      {
         this.battleIcon.removeEventListener(Event.CHANGE,this.onBattleIconChangeHandler);
         this.battleIcon.dispose();
         this.battleIcon = null;
         this.titleTF = null;
         this.subTitleTF = null;
         this.descriptionTF = null;
         this.headerBG = null;
         super.onDispose();
      }
      
      public function getContentHeight() : Number
      {
         return this.headerBG.height;
      }
      
      public function setData(param1:PortalEventHeaderVO) : void
      {
         this.titleTF.text = param1.title;
         this.subTitleTF.text = param1.subTitle;
         this.descriptionTF.text = param1.description;
         App.utils.commons.updateTextFieldSize(this.descriptionTF,false,true);
         this.battleIcon.source = RES_ICONS_PORTAL.PORTAL_GUI_MAPS_ICONS_BATTLETYPES_136X136_PORTAL_BATTLE;
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         this.headerBG.x = -param1 >> 1;
         this.headerBG.width = param1;
         if(App.stageSizeMgr.currentBreakPoint == StageBreakPointList.EXTRA_LARGE)
         {
            this.headerBG.height = HEADER_BG_HEIGHT_EXTRA_LARGE;
         }
         else
         {
            this.headerBG.height = HEADER_BG_HEIGHT;
         }
      }
      
      private function initialiaze() : void
      {
         this.titleTF.autoSize = TextFieldAutoSize.LEFT;
         this.battleIcon.addEventListener(Event.CHANGE,this.onBattleIconChangeHandler);
      }
      
      private function onBattleIconChangeHandler(param1:Event) : void
      {
         var _loc2_:Number = NaN;
         _loc2_ = -this.battleIcon.width >> 1;
         var _loc3_:int = _loc2_ + this.battleIcon.width + ICON_MARGIN_X;
         this.titleTF.x = _loc2_ - ICON_MARGIN_X - this.titleTF.width;
         this.battleIcon.x = _loc2_;
         this.subTitleTF.x = _loc3_;
         this.descriptionTF.x = _loc3_;
      }
   }
}
