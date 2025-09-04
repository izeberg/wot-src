package net.wg.white_tiger.gui.battle.views.ribbonsPanel
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.components.ribbon.constants.RibbonColors;
   import net.wg.gui.components.ribbon.data.RibbonSettingByType;
   import net.wg.gui.components.ribbon.data.RibbonSettings;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_EFFICIENCY_TYPES;
   
   public class WhiteTigerRibbonSettings extends RibbonSettings
   {
       
      
      public function WhiteTigerRibbonSettings(param1:String, param2:String)
      {
         super(param1,param2);
      }
      
      override protected function atlasInit() : void
      {
         super.atlasInit();
         var _loc1_:String = RibbonColors.RED;
         var _loc2_:String = RibbonColors.PURPLE;
         RIBBON_TYPES_MAP[WHITE_TIGER_BATTLE_EFFICIENCY_TYPES.CIRCUIT_OVERLOAD] = new RibbonSettingByType(_loc1_,BATTLEATLAS.RIBBONS_DAMAGE_BY_CIRCUIT_OVERLOAD,_loc1_,BATTLEATLAS.RIBBONS_DAMAGE_BY_CIRCUIT_OVERLOAD,1);
         RIBBON_TYPES_MAP[WHITE_TIGER_BATTLE_EFFICIENCY_TYPES.HYPERION] = new RibbonSettingByType(_loc1_,BATTLEATLAS.RIBBONS_DAMAGE_ENEMY,_loc2_,BATTLEATLAS.RIBBONS_DAMAGE_ENEMY_BLIND,1);
      }
   }
}
