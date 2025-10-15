package net.wg.portal.gui.battle.views.consumablesPanel
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.filters.GlowFilter;
   import flash.text.TextField;
   import net.wg.data.constants.generated.CONSUMABLES_PANEL_SETTINGS;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.views.consumablesPanel.events.ConsumablesButtonEvent;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IBattleEquipmentButtonGlow;
   import scaleform.gfx.TextFieldEx;
   
   public class BattleEquipmentButtonGlow extends BattleUIComponent implements IBattleEquipmentButtonGlow
   {
      
      private static const SHOW_GLOW_GREEN_STATE:String = "green";
      
      private static const SHOW_GLOW_GREEN_SPECIAL_STATE:String = "greenSpecial";
      
      private static const SHOW_GLOW_ORANGE_SPECIAL_STATE:String = "orangeSpecial";
      
      private static const NORMAL_TEXT_COLOR:uint = 13297644;
       
      
      public var tfContainer:MovieClip = null;
      
      public var hotkeyBg:Sprite = null;
      
      private var _textField:TextField = null;
      
      public function BattleEquipmentButtonGlow()
      {
         super();
         addFrameScript(0,this.goIdle);
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this._textField = this.tfContainer.bindKeyField;
         this._textField.textColor = NORMAL_TEXT_COLOR;
         TextFieldEx.setNoTranslate(this._textField,true);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         mouseEnabled = false;
         mouseChildren = false;
      }
      
      override protected function onDispose() : void
      {
         addFrameScript(0,null);
         stop();
         this._textField = null;
         this.hotkeyBg = null;
         this.tfContainer = null;
         super.onDispose();
      }
      
      public function hideGlow(param1:Boolean = true) : void
      {
      }
      
      public function setBindKeyText(param1:String) : void
      {
         this._textField.text = param1;
      }
      
      public function setBindKeyTextVisibility(param1:Boolean) : void
      {
         this.tfContainer.filters = !!param1 ? [] : [new GlowFilter(4473924,1,2,2,5,1,false,true)];
         this.hotkeyBg.visible = param1;
      }
      
      public function showGlow(param1:int, param2:Boolean = true) : void
      {
         switch(param1)
         {
            case CONSUMABLES_PANEL_SETTINGS.GLOW_ID_GREEN:
               gotoAndPlay(SHOW_GLOW_GREEN_STATE);
               break;
            case CONSUMABLES_PANEL_SETTINGS.GLOW_ID_GREEN_SPECIAL:
               gotoAndPlay(SHOW_GLOW_GREEN_SPECIAL_STATE);
               break;
            case CONSUMABLES_PANEL_SETTINGS.GLOW_ID_ORANGE_SPECIAL:
               gotoAndPlay(SHOW_GLOW_ORANGE_SPECIAL_STATE);
               break;
            default:
               stop();
         }
         this._textField.textColor = NORMAL_TEXT_COLOR;
      }
      
      private function goIdle() : void
      {
         stop();
         dispatchEvent(new Event(ConsumablesButtonEvent.GLOW_ON_IDLE_STATE));
      }
   }
}
