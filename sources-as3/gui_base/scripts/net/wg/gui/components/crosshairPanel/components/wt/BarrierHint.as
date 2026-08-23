package net.wg.gui.components.crosshairPanel.components.wt
{
   import flash.text.TextField;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class BarrierHint extends SimpleDisposable
   {
       
      
      public var bindKeyTf:TextField = null;
      
      public var hintTf:TextField = null;
      
      public function BarrierHint()
      {
         super();
         this.hintTf.text = INGAME_GUI.CROSSHAIR_HINT_WTBARRIER;
      }
      
      override protected function onDispose() : void
      {
         this.bindKeyTf = null;
         this.hintTf = null;
         super.onDispose();
      }
      
      public function setBindKey(param1:String) : void
      {
         this.bindKeyTf.text = param1;
      }
   }
}
