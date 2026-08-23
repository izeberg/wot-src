package net.wg.white_tiger.gui.battle.views.wtAbilityWidget
{
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   import net.wg.white_tiger.data.constants.WT_LINKAGES;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_VIEW_ALIASES;
   import net.wg.white_tiger.gui.battle.views.wtMissileWidget.WTMissileWidget;
   import net.wg.white_tiger.infrastructure.base.meta.IWTAbilityWidgetMeta;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WTAbilityWidgetMeta;
   
   public class WTAbilityWidget extends WTAbilityWidgetMeta implements IWTAbilityWidgetMeta, IDisplayableComponent
   {
       
      
      private var _missileWidget:WTMissileWidget = null;
      
      private var _stageWidth:Number;
      
      private var _stageHeight:Number;
      
      public function WTAbilityWidget()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._missileWidget)
         {
            removeChild(this._missileWidget);
         }
         this._missileWidget = null;
         super.onDispose();
      }
      
      public function as_addMissileWidget() : void
      {
         if(!this._missileWidget)
         {
            this._missileWidget = App.utils.classFactory.getComponent(WT_LINKAGES.WT_MISSILE_WIDGET,WTMissileWidget);
            addChild(this._missileWidget);
            registerFlashComponentS(this._missileWidget,WHITE_TIGER_BATTLE_VIEW_ALIASES.WT_MISSILE_WIDGET);
            this.updateMissileWidgetPosition();
         }
      }
      
      public function isCompVisible() : Boolean
      {
         return visible;
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
         visible = param1;
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         this._stageWidth = param1;
         this._stageHeight = param2;
         this.updateMissileWidgetPosition();
      }
      
      private function updateMissileWidgetPosition() : void
      {
         if(this._missileWidget)
         {
            this._missileWidget.updatePosition(this._stageWidth,this._stageHeight);
         }
      }
   }
}
