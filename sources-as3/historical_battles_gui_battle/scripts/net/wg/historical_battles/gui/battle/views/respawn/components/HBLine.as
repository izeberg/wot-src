package net.wg.historical_battles.gui.battle.views.respawn.components
{
   import flash.display.MovieClip;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class HBLine extends SimpleDisposable
   {
      
      public static const MODE_HEADER:uint = 1;
      
      public static const MODE_FOOTER:uint = 2;
      
      private static const LINE_WIDTH:Object = {};
      
      {
         LINE_WIDTH[MODE_HEADER] = {};
         LINE_WIDTH[MODE_HEADER][HB_STAGE_SIZE.EXTRA_SMALL] = 172;
         LINE_WIDTH[MODE_HEADER][HB_STAGE_SIZE.SMALL] = 172;
         LINE_WIDTH[MODE_HEADER][HB_STAGE_SIZE.MEDIUM] = 240;
         LINE_WIDTH[MODE_HEADER][HB_STAGE_SIZE.LARGE] = 240;
         LINE_WIDTH[MODE_HEADER][HB_STAGE_SIZE.EXTRA_LARGE] = 308;
         LINE_WIDTH[MODE_FOOTER] = {};
         LINE_WIDTH[MODE_FOOTER][HB_STAGE_SIZE.EXTRA_SMALL] = 478;
         LINE_WIDTH[MODE_FOOTER][HB_STAGE_SIZE.SMALL] = 692;
         LINE_WIDTH[MODE_FOOTER][HB_STAGE_SIZE.MEDIUM] = 692;
         LINE_WIDTH[MODE_FOOTER][HB_STAGE_SIZE.LARGE] = 692;
         LINE_WIDTH[MODE_FOOTER][HB_STAGE_SIZE.EXTRA_LARGE] = 1108;
      }
      
      public var line:MovieClip = null;
      
      private var _size:uint = 0;
      
      private var _mode:uint = 1;
      
      public function HBLine()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.line = null;
         super.onDispose();
      }
      
      public function setMode(param1:uint) : void
      {
         this._mode = param1;
      }
      
      public function updateSize(param1:uint) : void
      {
         if(this._size != param1)
         {
            this._size = param1;
            this.line.width = LINE_WIDTH[this._mode][this._size];
         }
      }
   }
}
