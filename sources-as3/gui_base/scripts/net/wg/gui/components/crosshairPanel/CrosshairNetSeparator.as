package net.wg.gui.components.crosshairPanel
{
   import flash.display.MovieClip;
   
   public class CrosshairNetSeparator extends MovieClip
   {
       
      
      private var _type:String = "";
      
      public function CrosshairNetSeparator()
      {
         super();
      }
      
      public function updateType(param1:String) : void
      {
         if(this._type != param1)
         {
            this._type = param1;
            gotoAndStop(param1);
         }
      }
   }
}
