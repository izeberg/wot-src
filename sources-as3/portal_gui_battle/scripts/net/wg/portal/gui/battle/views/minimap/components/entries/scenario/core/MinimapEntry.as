package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core
{
   import flash.display.MovieClip;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.managers.IAtlasManager;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class MinimapEntry extends BattleUIComponent
   {
       
      
      public var icon:MovieClip = null;
      
      public var highlight:MovieClip = null;
      
      private var _colorblindMode:Boolean = false;
      
      private var _atlasManager:IAtlasManager;
      
      private var _colorSchemeMgr:IColorSchemeManager;
      
      private var _iconType:String = null;
      
      private var _iconTypeColorblind:String = null;
      
      private var _backIcon:String = null;
      
      public function MinimapEntry()
      {
         this._atlasManager = App.atlasMgr;
         this._colorSchemeMgr = App.colorSchemeMgr;
         super();
      }
      
      override protected function initialize() : void
      {
         this._colorSchemeMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onSchemasUpdatedHandler);
         this.updateColorBlind();
         super.initialize();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.drawIconType();
         this.drawBackIcon();
      }
      
      override protected function onDispose() : void
      {
         this._colorSchemeMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onSchemasUpdatedHandler);
         this._atlasManager = null;
         this.icon.graphics.clear();
         this.icon = null;
         this.highlight.graphics.clear();
         this.highlight = null;
         this._colorSchemeMgr = null;
         super.onDispose();
      }
      
      private function updateColorBlind() : void
      {
         this.setColorBlindMode(this._colorSchemeMgr.getIsColorBlindS());
      }
      
      private function setColorBlindMode(param1:Boolean) : void
      {
         if(this._colorblindMode != param1)
         {
            this._colorblindMode = param1;
            invalidateState();
         }
      }
      
      private function drawIconType() : void
      {
         if(StringUtils.isEmpty(this._iconType))
         {
            return;
         }
         var _loc1_:String = this._iconType;
         if(this._colorblindMode && StringUtils.isNotEmpty(this._iconTypeColorblind))
         {
            _loc1_ = this._iconTypeColorblind;
         }
         this.icon.graphics.clear();
         this._atlasManager.drawGraphics(ATLAS_CONSTANTS.BATTLE_ATLAS,_loc1_,this.icon.graphics,Values.EMPTY_STR,true,false,true);
      }
      
      private function drawBackIcon() : void
      {
         if(StringUtils.isEmpty(this._backIcon))
         {
            return;
         }
         this._atlasManager.drawGraphics(ATLAS_CONSTANTS.BATTLE_ATLAS,this._backIcon,this.highlight.graphics,Values.EMPTY_STR,true,false,true);
      }
      
      public function set iconType(param1:String) : void
      {
         this._iconType = param1;
         this.drawIconType();
      }
      
      public function set iconTypeColorblind(param1:String) : void
      {
         this._iconTypeColorblind = param1;
         this.drawIconType();
      }
      
      public function set backIcon(param1:String) : void
      {
         this._backIcon = param1;
         this.drawBackIcon();
      }
      
      private function onSchemasUpdatedHandler(param1:ColorSchemeEvent) : void
      {
         this.updateColorBlind();
      }
   }
}
