package net.wg.gui.battle.views.decorativeCrosshair
{
   import flash.utils.Dictionary;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.generated.BATTLE_VIEW_ALIASES;
   import net.wg.data.constants.generated.DECORATIVE_CROSSHAIR_CONSTS;
   import net.wg.infrastructure.base.meta.IDecorativeCrosshairPanelMeta;
   import net.wg.infrastructure.base.meta.impl.DecorativeCrosshairPanelMeta;
   
   public class DecorativeCrosshairPanel extends DecorativeCrosshairPanelMeta implements IDecorativeCrosshairPanelMeta
   {
       
      
      private var _crosshairStorage:Dictionary;
      
      private var _crosshairType:int = 1;
      
      private var _isVisible:Boolean = true;
      
      public function DecorativeCrosshairPanel()
      {
         this._crosshairStorage = new Dictionary();
         super();
      }
      
      override protected function draw() : void
      {
         var _loc1_:BaseDecorativeCrosshair = null;
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            for each(_loc1_ in this._crosshairStorage)
            {
               _loc1_.updateScale(this._crosshairType);
            }
         }
      }
      
      override protected function onDispose() : void
      {
         App.utils.data.cleanupDynamicObject(this._crosshairStorage);
         this._crosshairStorage = null;
         super.onDispose();
      }
      
      override protected function updateVisibility() : void
      {
         this.visible = this._isVisible && _isCompVisible;
      }
      
      public function as_addDecorCrosshair(param1:String) : void
      {
         var _loc2_:String = null;
         var _loc3_:Class = null;
         var _loc4_:String = null;
         var _loc5_:BaseDecorativeCrosshair = null;
         switch(param1)
         {
            case DECORATIVE_CROSSHAIR_CONSTS.CONCENTRATION:
               _loc2_ = Linkages.CONCENTRATION_DECOR_CROSSHAIR;
               _loc3_ = ConcentrationDecorativeCrosshair;
               _loc4_ = BATTLE_VIEW_ALIASES.CONCENTRATION_DECORATIVE_CROSSHAIR;
               break;
            case DECORATIVE_CROSSHAIR_CONSTS.ACCURACY:
               _loc2_ = Linkages.ACCURACY_DECOR_CROSSHAIR;
               _loc3_ = AccuracyStackDecorativeCrosshair;
               _loc4_ = BATTLE_VIEW_ALIASES.ACCURACY_DECORATIVE_CROSSHAIR;
               break;
            case DECORATIVE_CROSSHAIR_CONSTS.PILLBOX_SIEGE:
               _loc2_ = Linkages.PILLBOX_SIEGE_DECOR_CROSSHAIR;
               _loc3_ = PillboxSiegeDecorativeCrosshair;
               _loc4_ = BATTLE_VIEW_ALIASES.PILLBOX_SIEGE_DECORATIVE_CROSSHAIR;
               break;
            case DECORATIVE_CROSSHAIR_CONSTS.OVERHEAT:
               _loc2_ = Linkages.OVERHEAT_DECOR_CROSSHAIR;
               _loc3_ = OverheatDecorativeCrosshair;
               _loc4_ = BATTLE_VIEW_ALIASES.OVERHEAT_DECORATIVE_CROSSHAIR;
               break;
            case DECORATIVE_CROSSHAIR_CONSTS.FURY:
               _loc2_ = Linkages.FURY_DECOR_CROSSHAIR;
               _loc3_ = FuryDecorativeCrosshair;
               _loc4_ = BATTLE_VIEW_ALIASES.FURY_DECORATIVE_CROSSHAIR;
               break;
            case DECORATIVE_CROSSHAIR_CONSTS.TEMPERATURE_GUN_OVERHEAT:
               _loc2_ = Linkages.TEMPERATURE_GUN_OVERHEAT_DECOR_CROSSHAIR;
               _loc3_ = TemperatureGunOverheatDecorativeCrosshair;
               _loc4_ = BATTLE_VIEW_ALIASES.TEMPERATURE_GUN_OVERHEAT_DECORATIVE_CROSSHAIR;
               break;
            default:
               return;
         }
         if(!this._crosshairStorage[_loc4_])
         {
            _loc5_ = App.utils.classFactory.getComponent(_loc2_,_loc3_);
            addChild(_loc5_);
            _loc5_.x = _loc5_.y = 0;
            this._crosshairStorage[_loc4_] = _loc5_;
            registerFlashComponentS(_loc5_,_loc4_);
         }
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         if(this._isVisible == param1)
         {
            return;
         }
         this._isVisible = param1;
         this.updateVisibility();
      }
      
      public function as_updateCrosshairType(param1:int) : void
      {
         this._crosshairType = param1;
         invalidateSize();
      }
      
      public function as_updateLayout(param1:int, param2:int) : void
      {
         this.x = param1;
         this.y = param2;
      }
   }
}
