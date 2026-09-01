package net.wg.white_tiger.gui.battle.views.minimap.entries
{
   import flash.text.TextField;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.views.minimap.MinimapEntryController;
   import net.wg.infrastructure.managers.IAtlasManager;
   
   public class WhiteTigerIndexedMinimapEntry extends BattleUIComponent
   {
       
      
      public var textField:TextField = null;
      
      protected var _atlasManager:IAtlasManager;
      
      public function WhiteTigerIndexedMinimapEntry()
      {
         this._atlasManager = App.atlasMgr;
         super();
         MinimapEntryController.instance.registerScalableEntry(this);
      }
      
      override protected function onDispose() : void
      {
         MinimapEntryController.instance.unregisterScalableEntry(this);
         this.textField = null;
         this._atlasManager = null;
         super.onDispose();
      }
   }
}
