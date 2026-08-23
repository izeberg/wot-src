package net.wg.gui.components.crosshairPanel.components.wt.components
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class PlasmaExtraDamageBraces extends SimpleDisposable
   {
      
      private static const BRACES_LBL_SHOW:String = "show";
      
      private static const BRACES_LBL_HIDE:String = "hide";
      
      private static const BRACES_LBL_END_POSTFIX:String = "_end";
      
      private static const X_OFFSET:int = 8;
       
      
      public var braces:MovieClip = null;
      
      private var _isBracesShown:Boolean = false;
      
      public function PlasmaExtraDamageBraces()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.braces = null;
      }
      
      public function layout(param1:int) : void
      {
         if(!this._isBracesShown)
         {
            return;
         }
         this.braces.rightBrace.x = param1 + X_OFFSET;
      }
      
      public function hideBraces(param1:Boolean = true) : void
      {
         if(!this._isBracesShown)
         {
            return;
         }
         this._isBracesShown = false;
         if(param1)
         {
            gotoAndPlay(BRACES_LBL_HIDE);
         }
         else
         {
            gotoAndStop(BRACES_LBL_HIDE + BRACES_LBL_END_POSTFIX);
         }
      }
      
      public function showBraces(param1:Boolean = true) : void
      {
         if(this._isBracesShown)
         {
            return;
         }
         this._isBracesShown = true;
         if(param1)
         {
            gotoAndPlay(BRACES_LBL_SHOW);
         }
         else
         {
            gotoAndStop(BRACES_LBL_SHOW + BRACES_LBL_END_POSTFIX);
         }
      }
   }
}
