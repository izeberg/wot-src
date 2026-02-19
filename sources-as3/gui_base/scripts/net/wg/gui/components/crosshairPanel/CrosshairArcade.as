package net.wg.gui.components.crosshairPanel
{
   public class CrosshairArcade extends CrosshairWithCassette
   {
       
      
      private var _reloadTimeBlinkYPositions:Array;
      
      private var _abilityModifierXPositions:Array;
      
      public function CrosshairArcade()
      {
         this._reloadTimeBlinkYPositions = [9,39,10,39,22];
         this._abilityModifierXPositions = [160,211,160,155,155];
         super();
      }
      
      override protected function onDispose() : void
      {
         this._reloadTimeBlinkYPositions.splice(0,this._reloadTimeBlinkYPositions.length);
         this._reloadTimeBlinkYPositions = null;
         this._abilityModifierXPositions.splice(0,this._abilityModifierXPositions.length);
         this._abilityModifierXPositions = null;
         super.onDispose();
      }
      
      override protected function getReloadTimeBlinkYPos() : Array
      {
         return this._reloadTimeBlinkYPositions;
      }
      
      override protected function getAbilityModifierXPos() : Array
      {
         return this._abilityModifierXPositions;
      }
   }
}
