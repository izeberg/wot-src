package net.wg.portal.gui.battle.views.minimap.components.entries.vehicle
{
   import flash.display.Sprite;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.infrastructure.managers.IAtlasManager;
   
   public class VehicleAnimationMinimapEntry extends BattleUIComponent
   {
      
      private static const GREEN_ALLY_ORIGIN_KEY:String = "ally_green";
      
      private static const GREEN_ALLY_OVERRIDE_KEY:String = "teamKiller_blue";
       
      
      public var atlasContainer:Sprite = null;
      
      private var _atlasManager:IAtlasManager;
      
      public function VehicleAnimationMinimapEntry()
      {
         this._atlasManager = App.atlasMgr;
         super();
      }
      
      override protected function onDispose() : void
      {
         this._atlasManager = null;
         this.atlasContainer = null;
         super.onDispose();
      }
      
      public function drawEntry(param1:String) : void
      {
         if(param1.search(GREEN_ALLY_ORIGIN_KEY) != Values.DEFAULT_INT)
         {
            param1 = param1.replace(GREEN_ALLY_ORIGIN_KEY,GREEN_ALLY_OVERRIDE_KEY);
         }
         this._atlasManager.drawGraphics(ATLAS_CONSTANTS.BATTLE_ATLAS,param1,this.atlasContainer.graphics,"",true);
      }
   }
}
