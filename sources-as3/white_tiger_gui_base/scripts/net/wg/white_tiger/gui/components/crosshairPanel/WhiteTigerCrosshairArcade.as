package net.wg.white_tiger.gui.components.crosshairPanel
{
   import flash.display.MovieClip;
   import net.wg.gui.components.crosshairPanel.CrosshairArcade;
   
   public class WhiteTigerCrosshairArcade extends CrosshairArcade implements IWhiteTigerCrosshair
   {
       
      
      public var arcadePlasmaIndicator:ArcadePlasmaIndicator = null;
      
      public var explosiveShot:MovieClip = null;
      
      public function WhiteTigerCrosshairArcade()
      {
         super();
         this.arcadePlasmaIndicator.netType = this.netType;
         this.explosiveShot.visible = false;
      }
      
      override protected function onDispose() : void
      {
         if(this.arcadePlasmaIndicator)
         {
            this.arcadePlasmaIndicator = null;
         }
         if(this.explosiveShot)
         {
            this.explosiveShot = null;
         }
         super.onDispose();
      }
      
      override public function setNetType(param1:Number) : void
      {
         super.setNetType(param1);
         if(this.netType != param1)
         {
            this.arcadePlasmaIndicator.netType = this.netType;
            this.arcadePlasmaIndicator.updatePlasmaIndicatorSize(this.netType);
         }
      }
      
      public function showPlasmaIndicator(param1:Number, param2:Boolean, param3:String) : void
      {
         if(this.arcadePlasmaIndicator)
         {
            this.arcadePlasmaIndicator.showPlasma(param1,param2,param3);
         }
      }
      
      public function setExplosiveShotVisible(param1:Boolean) : void
      {
         if(this.explosiveShot)
         {
            this.explosiveShot.visible = param1;
         }
      }
   }
}
