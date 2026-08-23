package net.wg.white_tiger.gui.battle.views.staticMarkers
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class DistanceMarker extends BattleUIComponent
   {
      
      private static const METERS:String = "m";
       
      
      public var marker:MovieClip = null;
      
      public var distanceText:TextField = null;
      
      private var _distance:Number;
      
      public function DistanceMarker()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.marker = null;
         this.distanceText = null;
         super.onDispose();
      }
      
      public function setDistance(param1:Number) : void
      {
         if(this._distance != param1)
         {
            this._distance = param1;
            this.distanceText.text = param1 + METERS;
         }
      }
      
      public function init() : void
      {
      }
      
      public function setActiveState(param1:int) : void
      {
      }
      
      public function setAlpha(param1:Number) : void
      {
      }
      
      public function setEntityIndex(param1:int) : void
      {
      }
   }
}
