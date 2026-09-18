package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.MECHANICS_WIDGET_CONST;
   import net.wg.infrastructure.base.meta.ISpecBoostModeWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.SpecBoostModeWidgetMeta;
   
   public class SpecBoostModeWidget extends SpecBoostModeWidgetMeta implements ISpecBoostModeWidgetMeta
   {
      
      private static const PROGRESSION_MAX_FRAME:int = 100;
       
      
      public var forwardProgress:MovieClip;
      
      public var reverseProgress:MovieClip;
      
      public var icon:MovieClip;
      
      private var _mechanicVariant:String = null;
      
      public function SpecBoostModeWidget()
      {
         super();
         blendMode = BlendMode.SCREEN;
      }
      
      override protected function applyState(param1:String, param2:Boolean) : void
      {
         super.applyState(param1,param2);
         this.icon.gotoAndStop(this._mechanicVariant);
      }
      
      override protected function onDispose() : void
      {
         this.forwardProgress = null;
         this.reverseProgress = null;
         this.icon = null;
         super.onDispose();
      }
      
      override protected function getInitialState() : String
      {
         return MECHANICS_WIDGET_CONST.IDLE;
      }
      
      override protected function getHotKeyVisibility() : Boolean
      {
         var _loc1_:Boolean = super.getHotKeyVisibility();
         return _loc1_ && this.state == MECHANICS_WIDGET_CONST.READY;
      }
      
      public function as_setActiveProgress(param1:Number) : void
      {
         this.reverseProgress.gotoAndStop(PROGRESSION_MAX_FRAME * param1);
      }
      
      public function as_setPreparingProgress(param1:Number) : void
      {
         this.forwardProgress.gotoAndStop(PROGRESSION_MAX_FRAME * param1);
      }
      
      public function as_setMechanicVariant(param1:String) : void
      {
         if(param1 == this._mechanicVariant)
         {
            return;
         }
         this._mechanicVariant = param1;
         this.icon.gotoAndStop(param1);
      }
   }
}
