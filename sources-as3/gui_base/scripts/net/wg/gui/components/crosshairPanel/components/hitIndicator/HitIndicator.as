package net.wg.gui.components.crosshairPanel.components.hitIndicator
{
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class HitIndicator extends SimpleDisposable
   {
       
      
      public var hitMarker0:HitArrow;
      
      public var hitMarker1:HitArrow;
      
      public var hitMarker2:HitArrow;
      
      public var hitMarker3:HitArrow;
      
      public function HitIndicator()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.hitMarker0.dispose();
         this.hitMarker1.dispose();
         this.hitMarker2.dispose();
         this.hitMarker3.dispose();
         this.hitMarker0 = null;
         this.hitMarker1 = null;
         this.hitMarker2 = null;
         this.hitMarker3 = null;
         super.onDispose();
      }
      
      public function show(param1:String) : void
      {
         this.hitMarker0.show(param1);
         this.hitMarker1.show(param1);
         this.hitMarker2.show(param1);
         this.hitMarker3.show(param1);
      }
   }
}
