package net.wg.gui.components.controls
{
   import flash.display.Sprite;
   import scaleform.clik.utils.Padding;
   
   public class ButtonSmallGray extends SoundButtonEx
   {
       
      
      public var bgMcTile:BitmapFill = null;
      
      public var border:Sprite = null;
      
      public function ButtonSmallGray()
      {
         super();
      }
      
      override protected function preInitialize() : void
      {
         super.preInitialize();
         focusable = true;
         disabledFillPadding = new Padding(1,1,0,0);
         _stateMap["down_out"] = ["down_out","out","up"];
      }
      
      override protected function onDispose() : void
      {
         this.bgMcTile.dispose();
         this.bgMcTile = null;
         this.border = null;
         super.onDispose();
      }
      
      override protected function updateSize() : void
      {
         if(this.bgMcTile != null)
         {
            this.bgMcTile.x = bgMc.x;
            this.bgMcTile.y = bgMc.y;
            this.bgMcTile.scaleX = 1 / this.scaleX;
            this.bgMcTile.scaleY = 1 / this.scaleY;
            this.bgMcTile.widthFill = Math.round(bgMc.width * this.scaleX);
            this.bgMcTile.heightFill = Math.round(bgMc.height * this.scaleY);
         }
         super.updateSize();
      }
      
      override protected function setState(param1:String) : void
      {
         var _loc2_:Boolean = _state == "down" && param1 == "out";
         param1 = !!_loc2_ ? "down_out" : param1;
         super.setState(param1);
      }
   }
}
