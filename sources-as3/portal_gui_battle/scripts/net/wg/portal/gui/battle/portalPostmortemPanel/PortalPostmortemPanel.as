package net.wg.portal.gui.battle.portalPostmortemPanel
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.InvalidationType;
   import net.wg.portal.infrastructure.base.meta.IPortalPostmortemPanelMeta;
   import net.wg.portal.infrastructure.base.meta.impl.PortalPostmortemPanelMeta;
   import net.wg.utils.StageBreakPointList;
   
   public class PortalPostmortemPanel extends PortalPostmortemPanelMeta implements IPortalPostmortemPanelMeta
   {
      
      private static const TEXT_FIELDS_WIDTH:uint = 600;
      
      private static const SCALE_SMALL:Number = 0.7;
      
      private static const TIMER_BOTTOM:uint = 305;
      
      private static const TIMER_BOTTOM_SMALL:uint = 215;
      
      private static const DEAD_TF_Y_SHIFT:uint = 80;
      
      private static const DEAD_TF_Y_SHIFT_SMALL:uint = 54;
      
      private static const RESPAWN_TF_Y_SHIFT:uint = 27;
      
      private static const RESPAWN_TF_Y_SHIFT_SMALL:uint = 22;
      
      private static const WAIT_TF_Y_SHIFT:uint = 33;
      
      private static const WAIT_TF_Y_SHIFT_SMALL:uint = 27;
      
      private static const DEAD_TF_SIZE:uint = 20;
      
      private static const DEAD_TF_SIZE_SMALL:uint = 16;
      
      private static const RESPAWN_TF_SIZE:uint = 16;
      
      private static const RESPAWN_TF_SIZE_SMALL:uint = 14;
      
      private static const WAIT_TF_SIZE:uint = 22;
      
      private static const WAIT_TF_SIZE_SMALL:uint = 18;
       
      
      public var timer:PostmortemTimer = null;
      
      public var deadTF:TextField = null;
      
      public var respawnTF:TextField = null;
      
      public var waitTF:TextField = null;
      
      public var neurons:Sprite = null;
      
      public var bg:Sprite = null;
      
      private var _stageWidth:int = 0;
      
      private var _stageHeight:int = 0;
      
      public function PortalPostmortemPanel()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.deadTF.text = PORTAL_BATTLE.POSTMORTEM_DEADMSG;
         this.respawnTF.text = PORTAL_BATTLE.POSTMORTEM_RESPAWNMSG;
         this.waitTF.text = PORTAL_BATTLE.POSTMORTEM_WAITMSG;
      }
      
      override protected function draw() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:TextFormat = null;
         super.draw();
         if(this._stageWidth != 0 && this._stageHeight != 0 && isInvalid(InvalidationType.POSITION))
         {
            this.bg.width = this._stageWidth;
            this.bg.height = this._stageHeight;
            _loc1_ = App.stageSizeMgr.currentBreakPoint == StageBreakPointList.EXTRA_SMALL;
            _loc2_ = !!_loc1_ ? Number(SCALE_SMALL) : Number(1);
            this.neurons.scaleX = this.neurons.scaleY = _loc2_;
            this.timer.scaleX = this.timer.scaleY = _loc2_;
            this.neurons.x = this._stageWidth >> 1;
            this.neurons.y = this._stageHeight - this.neurons.height | 0;
            _loc3_ = !!_loc1_ ? Number(TIMER_BOTTOM_SMALL) : Number(TIMER_BOTTOM);
            this.timer.x = this._stageWidth >> 1;
            this.timer.y = this._stageHeight - _loc3_ | 0;
            _loc4_ = this.deadTF.getTextFormat();
            _loc4_.size = !!_loc1_ ? DEAD_TF_SIZE_SMALL : DEAD_TF_SIZE;
            this.deadTF.setTextFormat(_loc4_);
            _loc4_ = this.respawnTF.getTextFormat();
            _loc4_.size = !!_loc1_ ? RESPAWN_TF_SIZE_SMALL : RESPAWN_TF_SIZE;
            this.respawnTF.setTextFormat(_loc4_);
            _loc4_ = this.waitTF.getTextFormat();
            _loc4_.size = !!_loc1_ ? WAIT_TF_SIZE_SMALL : WAIT_TF_SIZE;
            this.waitTF.setTextFormat(_loc4_);
            this.deadTF.x = this.respawnTF.x = this.waitTF.x = this._stageWidth - TEXT_FIELDS_WIDTH >> 1;
            this.deadTF.y = this.timer.y + (!!_loc1_ ? DEAD_TF_Y_SHIFT_SMALL : DEAD_TF_Y_SHIFT) | 0;
            this.respawnTF.y = this.deadTF.y + (!!_loc1_ ? RESPAWN_TF_Y_SHIFT_SMALL : RESPAWN_TF_Y_SHIFT) | 0;
            this.waitTF.y = this.respawnTF.y + (!!_loc1_ ? WAIT_TF_Y_SHIFT_SMALL : WAIT_TF_Y_SHIFT) | 0;
         }
      }
      
      override protected function onDispose() : void
      {
         this.timer.dispose();
         this.timer = null;
         this.deadTF = null;
         this.respawnTF = null;
         this.waitTF = null;
         this.neurons = null;
         this.bg = null;
         super.onDispose();
      }
      
      public function as_setTimer(param1:int) : void
      {
         if(param1 > 0)
         {
            this.timer.updateRadialTimer(param1,0);
         }
         else
         {
            this.timer.stopTimer();
         }
      }
      
      public function updateStage(param1:int, param2:int) : void
      {
         if(this._stageWidth != param1 || this._stageHeight != param2)
         {
            this._stageWidth = param1;
            this._stageHeight = param2;
            invalidate(InvalidationType.POSITION);
         }
      }
   }
}
