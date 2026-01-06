package net.wg.gui.lobby.epicBattles.components
{
   import flash.events.Event;
   import net.wg.data.constants.SoundManagerStates;
   import net.wg.data.constants.SoundTypes;
   import net.wg.gui.lobby.epicBattles.data.EpicBattlesWidgetVO;
   import net.wg.infrastructure.base.meta.IEpicBattlesWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.EpicBattlesWidgetMeta;
   import scaleform.clik.constants.InvalidationType;
   
   public class EpicBattlesWidget extends EpicBattlesWidgetMeta implements IEpicBattlesWidgetMeta
   {
       
      
      public var button:EpicBattlesWidgetButton = null;
      
      public var buttonIntro:EpicBattlesWidgetIntroButton = null;
      
      private var _data:EpicBattlesWidgetVO = null;
      
      public function EpicBattlesWidget()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.utils.commons.addEmptyHitArea(this);
         this.button.visible = this.buttonIntro.visible = false;
         this.button.addEventListener(EpicBattlesWidgetBaseButton.CLICK,this.onClickHandler);
         this.buttonIntro.addEventListener(EpicBattlesWidgetBaseButton.CLICK,this.onClickHandler);
         App.stage.addEventListener(Event.RESIZE,this.onStageResizeHandler,false,0,true);
         this.mouseEnabled = false;
      }
      
      override protected function onDispose() : void
      {
         App.stage.removeEventListener(Event.RESIZE,this.onStageResizeHandler);
         this.button.removeEventListener(EpicBattlesWidgetBaseButton.CLICK,this.onClickHandler);
         this.button.dispose();
         this.button = null;
         this.buttonIntro.removeEventListener(EpicBattlesWidgetBaseButton.CLICK,this.onClickHandler);
         this.buttonIntro.dispose();
         this.buttonIntro = null;
         if(this._data)
         {
            this._data.dispose();
            this._data = null;
         }
         super.onDispose();
      }
      
      override protected function setData(param1:EpicBattlesWidgetVO) : void
      {
         this._data = param1;
         this.button.setData(param1);
         this.buttonIntro.visible = param1.isSupplyHint;
         this.button.visible = !param1.isSupplyHint;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.validateSize();
         }
      }
      
      private function validateSize() : void
      {
         this.button.updateSize();
         this.buttonIntro.updateSize();
      }
      
      override public function get marginRight() : int
      {
         return this.button.marginRight;
      }
      
      override public function get marginLeft() : int
      {
         return this.button.marginLeft;
      }
      
      override public function get width() : Number
      {
         return this.button.width;
      }
      
      private function onClickHandler(param1:Event) : void
      {
         App.soundMgr.playControlsSnd(SoundManagerStates.SND_PRESS,SoundTypes.NORMAL_BTN,null);
         onWidgetClickS();
      }
      
      private function onStageResizeHandler(param1:Event) : void
      {
         invalidateSize();
      }
   }
}
