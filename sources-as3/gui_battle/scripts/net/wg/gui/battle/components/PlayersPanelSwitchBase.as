package net.wg.gui.battle.components
{
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.buttons.interfaces.IClickButtonHandler;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.panelSwitch.PlayersPanelSwitchButton;
   
   public class PlayersPanelSwitchBase extends BattleUIComponent implements IClickButtonHandler
   {
      
      protected static const DISABLED_ALPHA:Number = 0.5;
       
      
      public var hidenBt:PlayersPanelSwitchButton = null;
      
      public var shortBt:PlayersPanelSwitchButton = null;
      
      public var mediumBt:PlayersPanelSwitchButton = null;
      
      public var longBt:PlayersPanelSwitchButton = null;
      
      public var fullBt:PlayersPanelSwitchButton = null;
      
      protected var bgCombine:BattleAtlasSprite = null;
      
      protected var state:int = -1;
      
      protected var selectedBt:PlayersPanelSwitchButton = null;
      
      private var _isInteractive:Boolean = false;
      
      private var _isFirstRun:Boolean = true;
      
      public function PlayersPanelSwitchBase()
      {
         super();
         this.bgCombine = new BattleAtlasSprite();
         addChild(this.bgCombine);
         alpha = DISABLED_ALPHA;
      }
      
      override protected function onDispose() : void
      {
         this.setIsInteractive(false);
         this.bgCombine = null;
         this.hidenBt.dispose();
         this.shortBt.dispose();
         this.mediumBt.dispose();
         this.longBt.dispose();
         this.fullBt.dispose();
         this.hidenBt = null;
         this.shortBt = null;
         this.mediumBt = null;
         this.longBt = null;
         this.fullBt = null;
         this.selectedBt = null;
         super.onDispose();
      }
      
      public function onButtonClick(param1:Object) : void
      {
      }
      
      public function setIsInteractive(param1:Boolean) : void
      {
         if(this._isInteractive == param1)
         {
            return;
         }
         alpha = !!param1 ? Number(1) : Number(DISABLED_ALPHA);
         this.toggleCombineBg(!param1);
         this.toggleInteractiveElements(param1);
         if(param1)
         {
            this.hidenBt.addClickCallBack(this);
            this.shortBt.addClickCallBack(this);
            this.mediumBt.addClickCallBack(this);
            this.longBt.addClickCallBack(this);
            this.fullBt.addClickCallBack(this);
         }
         this._isInteractive = param1;
      }
      
      public function setState(param1:int) : void
      {
         if(this._isFirstRun)
         {
            this.toggleCombineBg(!this._isInteractive);
            this.toggleInteractiveElements(this._isInteractive);
            this._isFirstRun = false;
         }
      }
      
      protected function toggleInteractiveElements(param1:Boolean) : void
      {
         var _loc2_:Function = !!param1 ? addChild : removeChild;
         _loc2_(this.hidenBt);
         _loc2_(this.shortBt);
         _loc2_(this.mediumBt);
         _loc2_(this.longBt);
         _loc2_(this.fullBt);
      }
      
      private function toggleCombineBg(param1:Boolean) : void
      {
         this.bgCombine.visible = param1;
         if(this.selectedBt == this.hidenBt)
         {
            this.bgCombine.imageName = BATTLEATLAS.PLAYERS_SWITCH_0;
         }
         else if(this.selectedBt == this.shortBt)
         {
            this.bgCombine.imageName = BATTLEATLAS.PLAYERS_SWITCH_1;
         }
         else if(this.selectedBt == this.mediumBt)
         {
            this.bgCombine.imageName = BATTLEATLAS.PLAYERS_SWITCH_2;
         }
         else if(this.selectedBt == this.longBt)
         {
            this.bgCombine.imageName = BATTLEATLAS.PLAYERS_SWITCH_3;
         }
         else
         {
            this.bgCombine.imageName = BATTLEATLAS.PLAYERS_SWITCH_4;
         }
      }
   }
}
