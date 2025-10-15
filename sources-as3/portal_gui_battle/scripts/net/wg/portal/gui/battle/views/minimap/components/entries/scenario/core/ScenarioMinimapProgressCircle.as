package net.wg.portal.gui.battle.views.minimap.components.entries.scenario.core
{
   import flash.display.MovieClip;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.ATLAS_CONSTANTS;
   import net.wg.gui.battle.components.BaseProgressCircle;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.managers.IAtlasManager;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class ScenarioMinimapProgressCircle extends BaseProgressCircle
   {
      
      private static const NORMAL_STATE:String = "normal";
      
      private static const PRECISION:Number = 0.005;
      
      private static const INV_FRAME:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      private static const TOTAL_FRAMES:int = 181;
      
      private static const ICON_SIZE:uint = 50;
       
      
      public var icon:MovieClip = null;
      
      public var highlight:MovieClip = null;
      
      private var _progress:Number = 0;
      
      private var _atlasManager:IAtlasManager;
      
      private var _colorSchemeMgr:IColorSchemeManager;
      
      private var _iconType:String = null;
      
      private var _iconTypeColorblind:String = null;
      
      private var _backIcon:String = null;
      
      public function ScenarioMinimapProgressCircle()
      {
         this._atlasManager = App.atlasMgr;
         this._colorSchemeMgr = App.colorSchemeMgr;
         super();
      }
      
      override public function updateProgress(param1:Number) : void
      {
         if(Math.abs(this._progress - param1) >= PRECISION)
         {
            this._progress = param1;
            currentProgressFrame = this._progress * TOTAL_FRAMES >> 0;
            invalidate(INV_FRAME);
         }
      }
      
      override protected function initialize() : void
      {
         this._colorSchemeMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onSchemasUpdatedHandler);
         this.updateColorBlind();
         currentProgressFrame = 1;
         super.initialize();
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         super.draw();
         if(isInvalid(InvalidationType.STATE))
         {
            _loc1_ = !!colorblindMode ? COLORBLIND_STATE : NORMAL_STATE;
            if(state != _loc1_)
            {
               state = _loc1_;
            }
            invalidate(INV_FRAME);
         }
         if(isInvalid(INV_FRAME))
         {
            if(currentFrameLabel != state)
            {
               gotoAndStop(state);
            }
            if(progressCircle.currentFrame != curFrame)
            {
               progressCircle.gotoAndStop(curFrame);
            }
         }
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
         if(colorblindMode != param1)
         {
            colorblindMode = param1;
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
         if(colorblindMode && StringUtils.isNotEmpty(this._iconTypeColorblind))
         {
            _loc1_ = this._iconTypeColorblind;
         }
         this.icon.graphics.clear();
         this._atlasManager.drawGraphics(ATLAS_CONSTANTS.BATTLE_ATLAS,_loc1_,this.icon.graphics,Values.EMPTY_STR,true,false,true);
         this.icon.width = this.icon.height = ICON_SIZE;
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
