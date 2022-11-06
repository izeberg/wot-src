package net.wg.infrastructure.managers.impl.tutorial
{
   import flash.utils.Dictionary;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.generated.TUTORIAL_EFFECT_BUILDERS;
   import net.wg.data.constants.generated.TUTORIAL_EFFECT_TYPES;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class BuilderTypeMapping
   {
      
      private static var _defaultMapping:Dictionary = null;
       
      
      public function BuilderTypeMapping()
      {
         super();
      }
      
      public static function getLnk(param1:String, param2:String) : String
      {
         if(StringUtils.isNotEmpty(param2))
         {
            App.utils.asserter.assert(Class(TUTORIAL_EFFECT_BUILDERS).hasOwnProperty(param2),"Custom builder name " + param2 + Errors.WASNT_FOUND);
            return TUTORIAL_EFFECT_BUILDERS[param2];
         }
         if(_defaultMapping == null)
         {
            _defaultMapping = getDefaultMaping();
         }
         App.utils.asserter.assert(param1 in _defaultMapping,"EffectBuilder linkage for effect type " + param1 + Errors.WASNT_FOUND);
         return _defaultMapping[param1];
      }
      
      private static function getDefaultMaping() : Dictionary
      {
         var _loc1_:Dictionary = new Dictionary();
         _loc1_[TUTORIAL_EFFECT_TYPES.HINT] = TUTORIAL_EFFECT_BUILDERS.DEFAULT_HINT;
         _loc1_[TUTORIAL_EFFECT_TYPES.BOOTCAMP_HINT] = TUTORIAL_EFFECT_BUILDERS.HIGHLIGHT;
         _loc1_[TUTORIAL_EFFECT_TYPES.DISPLAY] = TUTORIAL_EFFECT_BUILDERS.DISPLAY;
         _loc1_[TUTORIAL_EFFECT_TYPES.TWEEN] = TUTORIAL_EFFECT_BUILDERS.TWEEN;
         _loc1_[TUTORIAL_EFFECT_TYPES.CLIP] = TUTORIAL_EFFECT_BUILDERS.CLIP;
         _loc1_[TUTORIAL_EFFECT_TYPES.ENABLED] = TUTORIAL_EFFECT_BUILDERS.ENABLED;
         _loc1_[TUTORIAL_EFFECT_TYPES.OVERLAY] = TUTORIAL_EFFECT_BUILDERS.OVERLAY;
         _loc1_[TUTORIAL_EFFECT_TYPES.DEFAULT_OVERLAY] = TUTORIAL_EFFECT_BUILDERS.DEFAULT_OVERLAY;
         _loc1_[TUTORIAL_EFFECT_TYPES.LAYOUT] = TUTORIAL_EFFECT_BUILDERS.AMMO_PANEL;
         return _loc1_;
      }
   }
}
