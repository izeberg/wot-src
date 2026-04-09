package net.wg.historical_battles.gui.battle.views.minimap.components.entries
{
   import flash.display.Sprite;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.infrastructure.managers.IAtlasManager;
   
   public class HbMinimapEntry extends BattleUIComponent
   {
       
      
      public var atlasPlaceholder:Sprite = null;
      
      private var _atlasManager:IAtlasManager;
      
      public function HbMinimapEntry()
      {
         this._atlasManager = App.atlasMgr;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._atlasManager.drawGraphics(ATLAS_CONSTANTS.BATTLE_ATLAS,this.atlasItemName,this.atlasPlaceholder.graphics,Values.EMPTY_STR,true);
      }
      
      override protected function onDispose() : void
      {
         this.atlasPlaceholder = null;
         this._atlasManager = null;
         super.onDispose();
      }
      
      protected function get atlasItemName() : String
      {
         throw new AbstractException("HbMinimapEntry get atlasItemName" + Errors.ABSTRACT_INVOKE);
      }
      
      protected function get atlasItemAltName() : String
      {
         return Values.EMPTY_STR;
      }
   }
}
