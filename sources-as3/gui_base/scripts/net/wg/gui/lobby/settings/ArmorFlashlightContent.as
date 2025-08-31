package net.wg.gui.lobby.settings
{
   import flash.display.MovieClip;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.lobby.settings.vo.config.aim.AimSettingsArmorFlashlightDataVo;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class ArmorFlashlightContent extends MovieClip implements IDisposable
   {
      
      private static const COLOR_SCHEMA_PATH:String = "../maps/icons/settings/armorFlashlight/";
      
      private static const COLOR_SCHEMA:String = "armorFlashlightColorSchema";
      
      private static const OPACITY:String = "armorFlashlightOpacity";
      
      private static const FILL:String = "armorFlashlightFill";
      
      private static const RESOLUTION:String = "armorFlashlightResolutionScaling";
      
      private static const ID:String = "id";
      
      private static const NAME:String = "name";
      
      private static const COLOR_BLIND_PREFIX:String = "_cb";
       
      
      public var imgLoader:UILoaderAlt = null;
      
      private var _disposed:Boolean = false;
      
      private var _isColorBlind:Boolean = false;
      
      private var _schemaID:String = null;
      
      private var _pattern:String = null;
      
      private var _resolution:String = null;
      
      public function ArmorFlashlightContent()
      {
         super();
         mouseEnabled = false;
         mouseChildren = false;
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.imgLoader.dispose();
         this.imgLoader = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setData(param1:AimSettingsArmorFlashlightDataVo, param2:Object) : void
      {
         this.imgLoader.alpha = param2[OPACITY];
         this.drawColorSchema(param1,param2);
      }
      
      private function drawColorSchema(param1:AimSettingsArmorFlashlightDataVo, param2:Object) : void
      {
         this._schemaID = param1.armorFlashlightColorSchema.options[param2[COLOR_SCHEMA]][ID];
         this._pattern = param1.armorFlashlightFill.options[param2[FILL]][ID];
         this._resolution = param1.armorFlashlightResolutionScaling.options[param2[RESOLUTION]][NAME];
         this.redraw();
      }
      
      private function getPath() : String
      {
         if(this._schemaID == null)
         {
            return null;
         }
         var _loc1_:String = COLOR_SCHEMA_PATH + this._schemaID + "_" + this._pattern + "_" + this._resolution;
         if(this._isColorBlind)
         {
            _loc1_ += COLOR_BLIND_PREFIX;
         }
         return _loc1_ + ".png";
      }
      
      public function setIsColorBlind(param1:Boolean) : void
      {
         if(this._isColorBlind != param1)
         {
            this._isColorBlind = param1;
            this.redraw();
         }
      }
      
      private function redraw() : void
      {
         this.imgLoader.source = this.getPath();
      }
   }
}
