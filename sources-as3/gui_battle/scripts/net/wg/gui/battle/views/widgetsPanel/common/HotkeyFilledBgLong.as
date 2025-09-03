package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.Sprite;
   
   public class HotkeyFilledBgLong extends HotkeyFilledBgPlain
   {
      
      private static const HORIZONTAL_PADDING:int = 10;
       
      
      public var leftBg:Sprite = null;
      
      public var rightBg:Sprite = null;
      
      public var centerBg:Sprite = null;
      
      public function HotkeyFilledBgLong()
      {
         super();
         this.leftBg.x = HORIZONTAL_PADDING >> 1;
      }
      
      override protected function onDispose() : void
      {
         this.leftBg = null;
         this.rightBg = null;
         this.centerBg = null;
         super.onDispose();
      }
      
      override protected function updateSize(param1:int) : void
      {
         var _loc2_:int = param1 - HORIZONTAL_PADDING - this.centerBg.width >> 1;
         this.leftBg.width = this.rightBg.width = _loc2_;
         this.centerBg.x = this.leftBg.x + this.leftBg.width;
         this.rightBg.x = this.centerBg.x + this.centerBg.width;
      }
   }
}
